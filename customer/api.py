# Customer service

from flask import Flask
from flask_restful import Resource, Api

import json
import urllib.request

app = Flask(__name__)
api = Api(app)


class Customer(Resource):
    def get(self):
        return{
            'customers':['T. Geddes Grant',
            'IBM',
            'Wysinco',
            'United Fruit Company']
        }
api.add_resource(Customer, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
