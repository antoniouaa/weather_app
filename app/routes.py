from flask import render_template, flash, redirect
from app import app
from app.forms import QueryForm

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        flash(f"location received as {form.location.data}")
        return redirect(f"/{form.location.data}")
    return render_template("index.html", title="Home", form=form)


@app.route("/<location>", methods=["GET"])
def temp_fetch(location):
    return render_template("weather_report.html", title="Report", location=location)
