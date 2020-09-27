from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QueryForm
import requests

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for("stats_fetch", location=f"{form.location.data}"))
    return render_template("index.html", title="Home", form=form)


@app.route("/query/<location>", methods=["GET"])
def stats_fetch(location):
    url = app.config["BASE_URL"]
    key = app.config["API_KEY"]
    params = {
        "key" : key,
        "q" : location,
    }
    weather_request = requests.get(f"{url}/current.json", params=params).json()
    return render_template("weather_report.html", title="Report", location=location, response=weather_request)
