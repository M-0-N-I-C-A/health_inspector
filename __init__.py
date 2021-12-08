from flask import Flask, g, current_app, render_template, request

import sqlite3

import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/")
def base():
    # render the base.html template
    return render_template("base.html")

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    # render the submit.html template in the GET case
    if request.method == "GET":
        return render_template("submit.html")
    # call the insert_info() function 
    # and render the submit.html with parameters
    # in the POST case
    else:
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        height = request.form["height"]
        weight = request.form["weight"]
        systolic = request.form["systolic"]
        diastolic = request.form["diastolic"]
        chol = request.form["chol"]
        gluc = request.form["gluc"]
        smoke = request.form["smoke"]
        alcohol = request.form["alcohol"]
        active = request.form["active"]

        x = [[int(age), int(gender), int(height), float(weight), int(systolic), int(diastolic), int(chol), int(gluc), int(smoke), int(alcohol), int(active)]]

        model = pickle.load(open("cardio-model/model.pkl", 'rb'))
        r = model.predict(x) + 1

        return render_template('submit.html', risk=r, name=name)