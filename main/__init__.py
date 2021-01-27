from flask import Flask #import flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
load_dotenv() #look for .env file


app = Flask(__name__) #initialize a Flask instance
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app) #init the mongo instance

from .routes.routes import * #import all of the routes


