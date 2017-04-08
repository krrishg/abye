#!/usr/bin/python

from flask import Flask,request,jsonify, render_template
from request_handler import Requests

app = Flask(__name__)  # flask object
request = Requests()  # Request object that handles requests ; more in request_handler.py


# routing index to welcome page
@app.route("/")
def index():
    return render_template("welcome.html")


# returns about all loans
@app.route("/loan/")
def loan():
    return jsonify(request.get_loan())


# returns about a type of loan
@app.route('/loan/<string:loan_type>/')
def loan_type(loan_type):
    return  jsonify(request.get_loan(loan_type))


# returns about all deposit
@app.route('/deposit/')
def deposit():
    return jsonify(request.get_deposit())


# returns about a type of deposit
@app.route('/deposit/<string:deposit_type>/')
def deposit_type(deposit_type):
    return jsonify(request.get_deposit(deposit_type))

if __name__ == "__main__":
    app.run(debug=True)