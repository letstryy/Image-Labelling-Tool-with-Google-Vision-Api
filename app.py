#!/usr/bin/env python3
#Dependencies
import sys
from os import walk
import imghdr
import csv
import webbrowser
import doctext
import argparse
import json
from flask import jsonify
from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import send_file
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Googleapi.json"

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('labeller'))
    return render_template('login.html', error=error)

@app.route('/labeller')
def labeller():
    if (app.config["HEAD"] == len(app.config["FILES"])):
        return redirect(url_for('bye'))
    directory = app.config['IMAGES']
    image = app.config["FILES"][app.config["HEAD"]]
    labels = app.config["LABELS"]
    not_end = not(app.config["HEAD"] == len(app.config["FILES"]) - 1)
    first = app.config["HEAD"]
    bounds = doctext.render_doc_text(app.config["IMAGES"],app.config["FILES"][app.config["HEAD"]])
    return render_template('labeller.html', not_end=not_end, first=first, directory=directory, image=image, bounds=bounds, labels=labels, head=app.config["HEAD"] + 1, len=len(app.config["FILES"]))

@app.route('/next')
def next():
    image = app.config["FILES"][app.config["HEAD"]]
    app.config["HEAD"] = app.config["HEAD"] + 1
    with open(app.config["OUT"],'a') as f:
        for label in app.config["LABELS"]:
            f.write(image + "," +
            label["id"] + "," +
            label["name"] + "," +
            label["angle"] + "," +
            str(round(float(label["xMin"]))) + "," +
            str(round(float(label["xMax"]))) + "," +
            str(round(float(label["yMin"]))) + "," +
            str(round(float(label["gid"]))) + "," +
            str(round(float(label["yMax"]))) + "\n")
    app.config["LABELS"] = []
    return redirect(url_for('labeller'))

@app.route('/discard')
def discard():
    image = app.config["FILES"][app.config["HEAD"]]
    a = 'discard'
    app.config["HEAD"] = app.config["HEAD"] + 1
    with open(app.config["OUT"],'a') as f:
            f.write(image + "," +
             a + "," +
             a + "," +
             a + "," +
             a + "," +
             a + "," +
             a + "\n")
    app.config["LABELS"] = []
    return redirect(url_for('labeller'))

@app.route("/bye")
def bye():
    return send_file("taf.gif", mimetype='image/gif')

@app.route('/add/<id>')
def add(id):
    angle = request.args.get("angle")
    gid = request.args.get("gid")
    xMin = request.args.get("xMin")
    xMax = request.args.get("xMax")
    yMin = request.args.get("yMin")
    yMax = request.args.get("yMax")
    app.config["LABELS"].append({"id":id, "name":"", "xMin":xMin, "xMax":xMax, "yMin":yMin, "yMax":yMax, "gid":gid, "angle":angle})
    return redirect(url_for('labeller'))

@app.route('/remove/<id>')
def remove(id):
    index = int(id) - 1
    del app.config["LABELS"][index]
    for label in app.config["LABELS"][index:]:
        label["id"] = str(int(label["id"]) - 1)
    return redirect(url_for('labeller'))

@app.route('/label/<id>')
def label(id):
    name = request.args.get("name")
    app.config["LABELS"][int(id) - 1]["name"] = name
    return redirect(url_for('labeller'))

@app.route('/prev')
def prev():
    image = app.config["FILES"][app.config["HEAD"]]
    app.config["HEAD"] = app.config["HEAD"] - 1
    return redirect(url_for('labeller'))

@app.route('/image/<f>')
def images(f):
    images = app.config['IMAGES']
    return send_file(images + f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='specify the images directory')
    parser.add_argument("--out")
    args = parser.parse_args()
    directory = args.dir
    if directory[len(directory) - 1] != "/":
         directory += "/"
    app.config["IMAGES"] = directory
    app.config["LABELS"] = []
    files = None
    for (dirpath, dirnames, filenames) in walk(app.config["IMAGES"]):
        files = filenames
        break
    if files == None:
        print("No files")
        exit()
    app.config["FILES"] = files
    app.config["HEAD"] = 0
    if args.out == None:
        app.config["OUT"] = "out.csv"
    else:
        app.config["OUT"] = args.out
    print(files)
    with open("out.csv",'w') as f:
        f.write("image,id,name,xMin,xMax,yMin,yMax\n")
    app.jinja_env.cache = {}
    url = 'http://127.0.0.1:5000/'
    webbrowser.open_new(url)
    app.run(debug=True, threaded=True, use_reloader=False)
