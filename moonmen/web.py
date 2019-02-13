# Import packages
import os
from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__, static_url_path="/static/")

# Routes
@app.route("/")
def dashboard():
    if session.get("logged_in") or not os.environ["PROJECT_PASSWORD"]:
        return render_template("dashboard.html", projectname=os.environ["PROJECT_NAME"])
    else:
        return render_template("login.html", projectname=os.environ["PROJECT_NAME"])


@app.route("/tasks")
def tasks():
    if session.get("logged_in") or not os.environ["PROJECT_PASSWORD"]:
        return render_template("tasks.html", projectname=os.environ["PROJECT_NAME"])
    else:
        return render_template("login.html", projectname=os.environ["PROJECT_NAME"])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == os.environ["PROJECT_PASSWORD"]:
            session["logged_in"] = True
        else:
            flash("Wrong password!")

    return dashboard()


@app.route("/logout")
def logout():
    if os.environ["PROJECT_PASSWORD"]:
        if session.get("logged_in"):
            session["logged_in"] = False

    return dashboard()