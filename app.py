# import flask as Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Hello</h1>"

# if __name__ == '__main__':
#     app.run(debug=True) 

import requests
from flask import Flask, jsonify
import json

app = Flask(__name__)

x = requests.get('https://www.w3schools.com/python/module_requests.asp')

file = open("js.json")


@app.route("/")
def hello_world():
    return f"<p>Hello world! {x.text.strip()}</p>"

@app.route("/python")
def rest():
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
    

if __name__ == '__main__':
    app.run(debug=True)
