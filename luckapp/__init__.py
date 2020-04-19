import os
from flask import Flask, Blueprint

from luckapp.database import init_db

def registerBlueprints(app):
    from luckapp.v1.users.controllers import mod_user
    from luckapp.v1.prizes.controllers import mod_prize

    app.register_blueprint(mod_user)
    app.register_blueprint(mod_prize)

# def create_app():
app = Flask(__name__, instance_relative_config=False)
app.config.from_object(os.environ['APP_SETTINGS'])

with app.app_context():
    init_db()

    registerBlueprints(app)