from flask import Flask, json, jsonify, request
import locale
import requests

from currency import Currency
from articles import Articles

app=Flask(__name__)

locale.setlocale(locale.LC_ALL, "russian")
json_data = {}

@app.route("/")
def index():
    json_data = get_names_data()
    return json_data

@app.route("/currency")
def currency():
    res = Currency().getRates()
    print(res)
    return jsonify(res)

@app.route("/articles")
def articles():
    res = Articles().getArticles()
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    app.run()