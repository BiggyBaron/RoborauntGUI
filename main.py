#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
import urllib
import pymysql
from flask import Flask, render_template, request, Markup


app = Flask(__name__)  # Creating new flask app

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('layout.html', **locals())


@app.route("/boss/", methods=['GET', 'POST'])
def boss():
    return render_template('boss.html', **locals())


@app.route("/order/", methods=['GET', 'POST'])
def client():
    return render_template('client.html', **locals())


@app.route("/worker/", methods=['GET', 'POST'])
def boss1():
    return render_template('worker.html', **locals())


# Main flask app
if __name__ == "__main__":
    # It creates https access by last argument. It is need to be give to web-page permission to microphone
    app.run(host='0.0.0.0', port=8090)