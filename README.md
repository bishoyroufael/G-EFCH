# Germany | Egyptian Foreigner Citizens Hub
A simple web-app for gathering information about Egyptians living in Germany and storing them in a *SQLite* database.

# Information
The project aim is to help the Egyptian Embassy in Berlin gather information about Egyptians easily and on a voluntarily basis from the citizins side. 

The project was designed to be simple enough to handle user reports if hosted properly. As of 2017, the number of Egyptians reported in Germany was around 29,600 <sup>[1](https://en.wikipedia.org/wiki/Arabs_in_Germany)</sup>


This project was created as a single contained Flask app. Front end was based on an open-source form template <sup>[2](https://colorlib.com/wp/template/contact-form-11/)</sup>


A small API was designed to communicate with the database that is created on-disk to add users to the system. There's also some data analysis that runs after the user is added to the database to see the distribution of Egyptian citizins accross Germany. Currently such distribution is shown as a heatmap and cardogram.

# Usage

You need to have [Anaconda3](https://www.anaconda.com/products/distribution) installed on your machine to run the app in a virtual environment.

- From your terminal inside the parent directory run `conda env create -f env.yaml`
- Then run `conda activate G-EFCH`
- To run the flask app run `python src/app.py`


## TODOs/Improvements

- Improve security and prevention of the API abuse/MITM possibilies.
- Return proper error message to the UI for errors that are know. *(i.e user already registered, ...etc)*
- Add a feature to let the user update his previous record *(i.e user changed his job, location, company, ...etc)*
- Better structuring of the project/split up src/app.py
- Can we cache the latest statistics results instead of recomputing the stats for all users every time a new user is added? 
- Use [celery](https://github.com/celery/celery) alongside with [redis](https://redis.io/) to manage background heavy task instead of forking a new process to run in the background
- Adding more statistics and charts
