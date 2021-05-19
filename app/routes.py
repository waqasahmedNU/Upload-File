from flask import Blueprint
from flask_restful import Api
from app.datastore import DataStore

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(DataStore, 'data_store')
