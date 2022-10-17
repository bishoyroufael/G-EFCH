from flask import current_app as app, jsonify, request
from flask import redirect, render_template, url_for
from flask import Flask
from forms import InfoForm 
from schemas.base import db
from schemas.user import User
import geopandas as gpd
import mapclassify as mc
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt
from multiprocessing import Process
from utils import Utils
from schemas.city import City
from schemas.state import State
from shapely.geometry import Point
import pandas as pd

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")
db.init_app(app)


'''
WEB endpoints
'''
@app.route("/", methods=["GET", "POST"])
def form_add():
    form = InfoForm()
    qu = db.session.execute(db.select(State)).scalars().all()
    form.state.choices = [(state.id, state.name) for state in qu ]
    form.city.choices = [(city.id, city.name) for city in qu[0].cities] 

    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "form_add.jinja2", form=form, template="form-template", title="Information Form"
    )

@app.route("/stats", methods = ["GET"])
def stats_user():
    return render_template("user_stats.jinja2", title="Stats")


'''
Utils
'''

def update_assets():
    gdf = gpd.read_file("src/assets/DEU_adm1.shp")
    gdf['population'] = 0
    with app.app_context():
        users = db.session.execute(db.select(User).filter_by()).scalars().all()
        points = []

        for user in users:
            points.append((user.city.lon, user.city.lat))
            
            idx_n = gdf[  gdf["NAME_1"] == user.city.state.name ].index
            idx_vn = gdf[ gdf["VARNAME_1"] == user.city.state.name ].index

            idx = idx_n[0] if len(idx_n) > 0 else idx_vn[0]

            gdf.at[idx, 'population'] += 1


    df_points = pd.DataFrame({"geometry" : points})
    df_points["geometry"] = df_points["geometry"].apply(Point)
    df_points.total_bounds = gdf.total_bounds

    # Plot heatmap
    ax = gplt.kdeplot(df_points, cmap="Reds", clip=gdf, fill=True, thresh=0.05, projection=gcrs.AlbersEqualArea() )
    gplt.polyplot(gdf, zorder=1, ax=ax)

    plt.savefig("src/static/images/heatmap.png", dpi=600)


    # Cartogram
    scheme = mc.Quantiles(gdf['population'], k=3)
    ax = gplt.cartogram(
        gdf, scale='population', projection=gcrs.AlbersEqualArea(),
        legend=True, legend_var='hue',
        hue='population', scheme=scheme, cmap='Greens',
        limits=(0.9,1)
    )
    gplt.polyplot(gdf, facecolor='lightgray', edgecolor='white', ax=ax)

    plt.savefig("src/static/images/cartogram.png", dpi=600)


'''
API endpoints
'''
@app.route("/api/v1/add_user", methods=["GET", "POST"])
def add_user():
    form_params = request.form

    city = db.session.execute(db.select(City).filter_by(id=form_params["city"])).scalars().first()
    user = User(form_params["fname"], 
        form_params["lname"], 
        form_params["email"], 
        form_params["phone"],
        form_params["job"],
        form_params["company"])

    city.users.append(user)
    # db.session.add(user)
    db.session.commit()


    update_assets_process = Process(
            target=update_assets,
            daemon=True
        )
    update_assets_process.start()

    return ('OK', 200)

@app.route('/city/<state>', methods=["GET", "POST"])
def state(state):
    res = db.session.execute(db.select(State).filter_by(name=state)).scalars().first()
    if not res:
        return ('Not Found', 404)

    all_cities = [{"id": city.id, "name":city.name} for city in db.session.execute(db.select(City).filter_by(state_id=res.id)).scalars().all()]

    return jsonify({'cities': all_cities}) 


# TODO 
@app.route("/api/v1/update_user", methods=["GET", "POST"])
def update_user():
    return ('OK', 200)





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        Utils.add_states_countires_db(db)
    app.run(host="localhost", debug=True)