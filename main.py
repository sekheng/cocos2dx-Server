"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

import json
import os
import string
import logging

# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return show_logo()

@app.route('/store_score', methods=['POST'])
def store_score():
    return "Successful sotring of highscore"

@app.route('/get_topscore/<int:_limit_scores>',methods=['GET'])
def get_topscores(_limit_scores):
    response_dict = []
    return json.dumps(response_dict)

@app.route('/logo', methods=['GET'])
def show_logo():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')
    return render_template('main.html', user_image = full_filename)

@app.errorhandler(400)
def page_bad_request(e):
    logging.info('unexpected error: {}'.format(e), 400)
    return redirect('https://http.cat/400')

@app.errorhandler(403)
def page_not_forbidden(e):
    logging.info('unexpected error: {}'.format(e), 403)
    return redirect('https://http.cat/403')

@app.errorhandler(404)
def page_not_found(e):
    logging.info('unexpected error: {}'.format(e), 404)
    return redirect('https://http.cat/404')

@app.errorhandler(405)
def page_method_not_allowed(e):
    logging.info('unexpected error: {}'.format(e), 405)
    return redirect('https://http.cat/405')

@app.errorhandler(409)
def page_user_conflict(e):
    logging.info('unexpected error: {}'.format(e), 409)
    return redirect('https://http.cat/409')

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    logging.info('unexpected error: {}'.format(e), 500)
    return redirect('https://http.cat/500')
