from datetime import datetime as dt
from flask import Blueprint, current_app, request, render_template, make_response, jsonify

from luckapp.database import db_session
from luckapp.v1.users.models import User
from luckapp.v1.users.schemas import UserSchema

mod_user = Blueprint('/api/v1/users', __name__)

@current_app.route('/api/v1/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        #GET ALL USERS
        users_schema = UserSchema(many=True)       
        users = User.query.all()

        result = users_schema.dump(users)
        
        return make_response(jsonify({'data': result, 'status': 200}))

    if request.method == 'POST':
        #CREATE A USER
        data = request.get_json()

        if data:
            existing_user = User.query.filter(User.email == data['email']).first()
            if existing_user:
                return make_response(f"{data['email']} already exists.")
            
            new_user = User(full_name=data['full_name'], 
                email=data['email'], 
                birthday=dt.now(),
                updated_at=dt.now(),
                created_at=dt.now(),
                city=data['city'], 
                phone=data['phone'], 
                is_admin=data['is_admin'])
            db_session.add(new_user)
            db_session.commit()

            return make_response(f"{new_user} successfully created!", 200)
