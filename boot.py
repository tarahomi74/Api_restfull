from peewee import *
from flask import Flask
from model.model import Book ,database
from flask_peewee.rest import RestAPI, UserAuthentication
from flask_peewee.auth import Auth

app = Flask(__name__)
app.config.from_object(__name__)


api = RestAPI(app)

api.register(Book)

# auth = Auth(app, database)
# user_auth = UserAuthentication(auth)
# api = RestAPI(app, default_auth=user_auth)

api.setup()


if __name__ == '__main__':
    app.run(debug=True)

