#!/usr/bin/env python3
"""First flask app"""
from flask import Flask

hbnb = Flask(__name__)
@hbnb.route("/", strict_slashes=False)
def index():
	return "Hello HBNB"

if __name__ == "__main__":
	hbnb.run(host="0.0.0.0", port=5000)
