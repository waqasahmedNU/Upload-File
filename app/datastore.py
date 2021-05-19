from flask import request, make_response, jsonify, g
from flask_restful import Resource, current_app as app

from app.database import Database
from os.path import exists, join


class DataStore(Resource):
    def __init__(self):
        self.database = Database()

    def get(self):
        result = {}
        http_status = 200
        result['data'] = self.database.get(g.connection)
        response = make_response(jsonify(result), http_status)
        return response

    def post(self):
        result = {}
        http_status = 200

        required_parameters = ['name']
        parameters = request.form
        file_required_parameters = ['file']
        file = request.files

        result = self.parameter_validation(parameters, required_parameters)
        if result['status'] == 0:
            result = self.parameter_validation(file, file_required_parameters)
            if result['status'] == 0:
                save_file_path = join(app.config['UPLOAD_FOLDER'], file['file'].filename)
                if self.save_file(file['file'], save_file_path):
                    data = [parameters.get('name'), save_file_path]
                    self.database.add(g.connection, data)
                    result['status'] = 0
                    result['result'] = 'File uploaded successfully'
                else:
                    http_status = 500
                    result['status'] = -1
                    result['error'] = 'File uploaded error'
            else:
                http_status = 400
        else:
            http_status = 400

        response = make_response(jsonify(result), http_status)
        return response

    def parameter_validation(self, parameters, required_parameters):
        response = {'status': 0, 'error': ''}

        for required_parameter in required_parameters:
            if required_parameter not in parameters:
                response['status'] = -1
                # response['error'] = ''
                response['error'] += required_parameter + ', '

        if response['error'] is not '':
            response['error'] = response['error'][0:-2]
            response['error'] = 'Required Field(s): ' + response['error']
        else:
            del response['error']

        return response

    def save_file(self, file, save_file_path):
        try:
            with open(save_file_path, 'ab') as f:
                f.write(file.stream.read())
            return True
        except Exception as e:
            print('File Upload Error', e)
        return False