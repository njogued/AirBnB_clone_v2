#!/usr/bin/python3
"""Flask task 1"""
from flask import Flask


hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
def hbnb_index():
    return "Hello HBNB!"


@hbnb.route("/hbnb", strict_slashes=False)
def hbnb_display():
    return "HBNB"


@hbnb.route("/c/<text>", strict_slashes=False)
def c_variable(text):
    return "C " + text.replace("_", " ")


@hbnb.route("/python", strict_slashes=False)
@hbnb.route("/python/<var>", strict_slashes=False)
def python_variable(var="is cool"):
    text = var.replace("_", " ") if "_" in var else var
    return "Python " + text


@hbnb.route("/number/<int:n>", strict_slashes=False)
def display_int(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
