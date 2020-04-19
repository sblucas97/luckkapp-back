import base64
from datetime import datetime as dt
from flask import Blueprint, current_app, request, render_template, make_response, jsonify

from luckapp.database import db_session
from luckapp.v1.prizes.models import Prize
from luckapp.v1.prizes.schemas import PrizeSchema

mod_prize = Blueprint('/api/v1/prizes', __name__)

@current_app.route('/api/v1/prizes', methods=['GET', 'POST'])
def prizes():
    if request.method == 'GET':
        #GET ALL PRIZES
        prizes_schema = PrizeSchema(many=True)       
        prizes = Prize.query.all()

        result = prizes_schema.dump(prizes)
        
        return make_response(jsonify({'data': result, 'status': 200}))

    if request.method == 'POST':
        #CREATE A USER
        data = request.get_json()

        if data:
            new_prize = Prize(name=data['name'], 
                description=data['description'],
                amount=data['amount'], 
                img=data['img'].encode('utf-8'),
                created_at=dt.now(), 
                updated_at=dt.now())
            db_session.add(new_prize)
            db_session.commit()

            return make_response(f"{data['name']} successfully created!", 200)
