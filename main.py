"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, url_for, Response, redirect, make_response, request, jsonify, abort
# import requests failed miserably!

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Cocos2dx'

@app.errorhandler(404)
def page_not_found(e):
	return redirect('https://http.cat/404')

@app.errorhandler(400)
def page_forbidden(e):
	return redirect('https://http.cat/400')

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error because I messed up: {}'.format(e), 500
