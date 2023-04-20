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


@hbnb.route("/c/<variable_name>", strict_slashes=False)
def c_variable(variable_name):
    if "_" in variable_name:
        text = variable_name.replace("_", " ")
    else:
        text = variable_name
    return "C " + text


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
