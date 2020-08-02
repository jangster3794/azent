from .utils import *
from flask import jsonify, request, render_template, flash
from flask import current_app as application
import json
from datetime import datetime

@application.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'success': True, 'version': '1.0', 'time': datetime.utcnow()}), 200


@application.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        payload = request.form
        resp = register_university(payload)
        if not resp.get('success'):
            flash('Something went wrong.')
    return render_template('add_university.html')


@application.route('/search', methods=['GET'])
def search():
    resp = {'success': True, 'data': []}
    if request.args:
        resp = search_universities(request.args)
        if not resp.get('success'):
            flash('Something went wrong.')
    return render_template('search.html', resp=resp['data'])


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