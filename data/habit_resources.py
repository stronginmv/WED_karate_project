from flask_restful import abort, Resource
from data import db_session
from data.merit import Merit
from flask import jsonify


def abort_if_user_not_found(habit_id):
    session = db_session.create_session()
    news = session.query(Merit).get(habit_id)
    if not news:
        abort(404, message=f"Habit {habit_id} not found")


class MeritsResource(Resource):
    def get(self, habits_id):
        abort_if_user_not_found(habits_id)
        session = db_session.create_session()
        news = session.query(Merit).get(habits_id)
        return jsonify({'habit': news.to_dict(
            only=('id', 'type', 'period', 'about_link', 'count', 'reposts', 'creator'))})


class MeritsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(Merit).all()
        return jsonify({'habits': [item.to_dict(
            only=('id', 'type', 'period', 'about_link', 'count', 'reposts', 'creator')) for item in user]})
