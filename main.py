"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request, url_for, redirect
from google.appengine.ext import ndb
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

import json
import os
import string
import logging
from MyModel import *

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
    logging.info(request.headers)
    dataDictionary = request.get_json()
    if dataDictionary is None:
        logging.info("request data: " + request.data)
        dataDictionary = json.loads(request.data)
    logging.info(dataDictionary)
    createdHighScore = None
    if 'score' in dataDictionary:
        createdHighScore = HighScore.CreateHighscore(dataDictionary.get('score'), 'anonymous')
        createdHighScore.put()
    if 'name' in dataDictionary:
        createdHighScore.mName = dataDictionary.get('name')
        createdHighScore.put()
    return json.dumps(createdHighScore.to_dict())

@app.route('/get_topscore/<int:_limit_scores>',methods=['GET'])
def get_topscores(_limit_scores):
    response_dict = []
    highscrDB = HighScore.query(HighScore.isDeleted == False).order(-HighScore.mScore)
    #fetch this number of highscores!
    listOfHighScore = highscrDB.fetch(_limit_scores)
    for playerScore in listOfHighScore:
        playerScoreDict = { 'score' : playerScore.mScore, 'name' : playerScore.mName }
        response_dict.append(playerScoreDict)
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
