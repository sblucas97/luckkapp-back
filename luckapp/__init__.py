import os
from flask import Flask, Blueprint
from flask_mail import Mail

from luckapp.database import init_db

def registerBlueprints(app):
    from luckapp.v1.users.controllers import mod_user
    from luckapp.v1.prizes.controllers import mod_prize
    from luckapp.v1.email.controllers import mod_email

    app.register_blueprint(mod_user)
    app.register_blueprint(mod_prize)
    app.register_blueprint(mod_email)


app = Flask(__name__, instance_relative_config=False)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config.update(dict({"MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']}))

with app.app_context():
    init_db()
    mail = Mail(app)

    registerBlueprints(app)