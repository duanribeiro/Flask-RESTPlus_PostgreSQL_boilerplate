import json
from api import db
from flask_restplus import abort
from bson.objectid import ObjectId
from api.helpers import encrypt_password
from api.v1.blueprints.users.models import Users
import logging

logger = logging.getLogger(__name__)


class Users:

    def __init__(self):
        pass

    @staticmethod
    def get_all_users():
        response = []
        for row in Users.query.all():
            row_dict = row.__dict__
            del row_dict['_sa_instance_state']

            response.append(row_dict)
        return json.loads(response)

    @staticmethod
    def get_user(username):
        user = Users.query.filter_by(username=username).first()
        if user:
            user = user.__dict__
            del user['_sa_instance_state']

            logger.warning(user)
            return json.loads(response)
        return None

    @staticmethod
    def insert_user(payload):
        user = Users.query.filter_by(username=payload['username']).first()
        if user:
            return 'Username already exists'

        password = encrypt_password(payload['password'])

        new_user = Users(username=payload['username'], password=password)
        db.session.add(new_user)
        db.session.commit()

        return {"username": payload['username']}, 201

    # @classmethod
    # def update_user(cls, id, data):
    #     if not cls.get_user(id):
    #         abort(404, 'User not found')
    #
    #     if mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': data}):
    #         return '', 204
    #     abort(422, 'No user updated')
    #
    # @classmethod
    # def delete_user(cls, id):
    #     if mongo.db.users.delete_one({'_id': ObjectId(id)}).deleted_count:
    #         return '', 204
    #     abort(404, 'User not found')
