from flask import Flask, g, make_response, jsonify
from app.routes import api_blueprint
from app.config import Config

from app.database import Database


class App:
    def __init__(self):
       pass

    def init(self):
        app = Flask(__name__)
        app.config.from_object(Config)
        app.register_blueprint(api_blueprint, url_prefix='{prefix}'.format(prefix=app.config['REST_URL_PREFIX']))

        db_conn = Database()
        db_conn.create(app.config['DB_FILE'])

        @app.before_request
        def before_request():
            g.connection = db_conn.connect()

        @app.after_request
        def after_request(response):
            db_conn.close(g.connection)
            return response

        return app
