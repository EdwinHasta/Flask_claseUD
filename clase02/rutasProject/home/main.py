from flask import Flask, request, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello World</p>"

@app.route("/magic")
def magic_number():
  number = random.randint(0,9)
  return "<p>Hi, your magic number is {}".format(number)

@app.route("/person/<name>")
def hi_person(name):
  return "<p>Hi, {}".format(name)

@app.route("/login")
def login():
  data = request.args
  print(data)
  return "Hi, {} your password is {}".format(data['name'], data['password'])

@app.route("/template")
def template():
  name_site = "Hi, for variable"
  return render_template("hello.html", name=name_site)

