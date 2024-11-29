import json
from flask import Flask, jsonify, request
from flasgger import Swagger
from routes import plaid_blueprint

import config

server = Flask(__name__)
server.debug = config.DEBUG
Swagger(server)

server.register_blueprint(plaid_blueprint, url_prefix='/plaid')

@server.route('/', methods=['GET'])
def get_root():
  arr = ['endpoint works as expected']
  return jsonify(arr)

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)