#!/usr/bin/python3
"""Flask task 1"""
from flask import Flask


alxhbnb = Flask(__name__)


@alxhbnb.route("/", strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    alxhbnb.run(host="0.0.0.0", port=5000)
