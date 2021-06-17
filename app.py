from flask import Flask,render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

app = Flask(__name__)

#set up mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"

#route to render index.html 
@app.route("/")
def home():
    