from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler


app = Flask(__name__)
scheduler = APScheduler()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///CrawlerDB.db"
db = SQLAlchemy(app)


from Crawler import routes
