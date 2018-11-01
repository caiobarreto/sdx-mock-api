# -*- coding: utf-8 -*-

import time
from functools import wraps
from flask import Flask, Response, jsonify, request, json, make_response, send_file

app = Flask(__name__)

@app.route("/")
def hello():
    return "Mock Services <br /> Services avaible: /v1/storesaround <br /> /v1/stores/1 <br /> /v1/storessuggestions"


_request_delay = 2  # seconds

def read_file(filepath):
    with open(filepath) as f:
        payload = json.loads(f.read())
        return jsonify(payload)

@app.route('/v1/storesaround', methods=['GET'])
def storesaround():
    time.sleep(_request_delay)
    return read_file('jsons/v1/storesaround.json')

@app.route('/v1/stores/1', methods=['GET'])
def stores():
    time.sleep(_request_delay)
    return read_file('jsons/v1/stores.json')

@app.route('/v1/storessuggestions', methods=['GET'])
def storessuggestions():
    time.sleep(_request_delay)
    return read_file('jsons/v1/storessuggestions.json')