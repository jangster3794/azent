from .utils import *
from flask import jsonify, request
from flask import current_app as application
import json
from datetime import datetime

@application.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'success': True, 'version': '1.0', 'time': datetime.utcnow()}), 200


@application.route('/register', methods=['POST'])
def register():
    payload = json.loads(request.data)
    resp = register_university(payload)
    return jsonify(resp), 200


@application.route('/search', methods=['GET'])
def search():
    resp = search_universities(request.args)
    return jsonify(resp), 200


@application.route('/edit/<university_id>', methods=['POST'])
def edit(university_id):
    payload = json.loads(request.data)
    resp = edit_university_data(university_id, payload)
    db.session.commit()
    return jsonify(resp)

@application.route('/delete/<university_id>')
def delete(university_id):
    resp = delete_university(university_id)
    return jsonify(resp)