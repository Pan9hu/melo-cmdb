from flask import Flask
from flask_pymongo import PyMongo

from core.settings import settings


class Server:
    app = Flask(__name__)

    datasource = {}
    print("[INFO]: create data source list.")
    for item in settings["datasource"]:
        if item["type"] == "mongodb":
            uri = "mongodb://" + item["host"] + ":" + item["port"] + "/" + item["database"]
            mongo = PyMongo(app, uri)
            datasource[item["name"]] = mongo
            print("[INFO]: connect to '{}' as '{}'.".format(uri, item["name"]))
