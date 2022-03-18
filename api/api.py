import flask
import requests
from flask import Flask, request
import json
from dicttoxml import dicttoxml
from json import loads
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST','GET'])
def home():

    payload = request.data
    json_decode=json.loads(payload)
    add =   json_decode['address']
    apikey =  json_decode['key']
    output_format = json_decode['output_format']
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+add+'&key='+apikey+'&output_format='+output_format)
    if output_format == "xml":
        xml = dicttoxml(loads(r.text))
        return xml
    else:
        return r.text




app.run()