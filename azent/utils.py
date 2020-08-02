# Using FLaskSQLALCHEMY
from .models import db,Universities
from datetime import datetime as dt
from sqlalchemy import  func

def register_university(data):
    print(data)
    try:
        new_university = Universities(
            name=data['name'],
            alpha_two_code=data['alpha_two_code'],
            country=data['country'],
            domain=data['domain'],
            web_page=data['web_page'],
            created_at=dt.utcnow()
        )
        db.session.add(new_university)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    except Exception as e:
        return {'success': False, 'error': str(e)}
    return {'success': True, 'message': 'Registered.'}

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def search_universities(filters):
    pg = max(int(filters.get('pg', 0))-1, 0)
    r = int(filters.get('r', 5))
    search_query = []
    if filters.get('name'):
        search_query.append(func.lower(Universities.name).like("%{}%".format((filters['name']).lower())))
    if filters.get('alpha_two_code'):
        search_query.append(func.lower(Universities.alpha_two_code) == filters['alpha_two_code'].lower())
    if filters.get('domain'):
        search_query.append(func.lower(Universities.domain).like("%{}".format((filters['domain']).lower())))
    data = Universities.query.filter(*search_query).limit(r).offset(pg*r)
    result_dict = [row2dict(row) for row in data]
    return {'success': True, 'data': result_dict}

def edit_university_data(university_id, data):
    try:
        Universities.query.filter(Universities.id==university_id).update(data)
    except Exception as ex:
        return  {'success': False, 'error': str(ex)}
    return {'success': True, 'message': 'Updated.'}

def delete_university(university_id):
    try:
        Universities.query.filter(Universities.id==university_id).delete()
        db.session.commit()
    except Exception as ex:
        return {'success': False, 'error': str(ex)}
    return {'success': True, 'message': 'Deleted.'}