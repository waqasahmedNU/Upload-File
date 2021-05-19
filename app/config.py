import os
from os.path import join, abspath, dirname


class Config:
    REST_URL_PREFIX = '/api/'
    ROOT_DIR = dirname(dirname(abspath(__file__)))
    DB_FILE = join(ROOT_DIR, 'database/data.db')
    UPLOAD_FOLDER = join(ROOT_DIR, 'database')
    ALLOWED_EXTENSIONS = {'.csv'}

    def __init__(self, app):
        pass

    @staticmethod
    def init_app(app):
        pass