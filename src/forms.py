from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SelectField, TelField
import json


'''
Form Fields
'''
class InfoForm(FlaskForm):
    fname = StringField(
        render_kw={"placeholder": "First name*"}
    )

    lname = StringField(
        render_kw={"placeholder": "Last name*"}
    )

    phone = TelField(
        render_kw={"placeholder": "Phone number*"}
    )

    job = StringField(
        render_kw={"placeholder": "Job*"}
    )

    state = SelectField(
        choices=[],
        render_kw={"placeholder": "State*"}
    )

    city = SelectField(
        choices=[],
        render_kw={"placeholder": "City*"}
    )

    company = StringField(
        render_kw={"placeholder": "Company*"}
    )

    email = StringField(
        render_kw={"placeholder": "Email*"}
    )

    recaptcha = RecaptchaField()