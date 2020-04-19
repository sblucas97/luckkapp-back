from luckapp import mail, app
from flask import Blueprint, current_app, request, render_template, make_response, jsonify

from luckapp.v1.email.models import CreateMessage

mod_email = Blueprint('/api/v1/email', __name__)

@current_app.route('/api/v1/email/registration', methods=['GET', 'POST'])
def email():
    #GET EMAIL DATA
    data = request.get_json()
    if data:
        mail.send(CreateMessage(data, 'registration_email'))    
        return make_response("Email sent")
