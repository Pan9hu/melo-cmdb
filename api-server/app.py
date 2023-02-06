from flask import Flask
from pymongo import auth

from api import account_api
from api import auth_api
from api import group_api

app = Flask(__name__)

app.register_blueprint(auth_api.bp_auth)
app.register_blueprint(group_api.bp_group)
app.register_blueprint(account_api.bp_account)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Melo CMDB!'


if __name__ == '__main__':
    app.run()
