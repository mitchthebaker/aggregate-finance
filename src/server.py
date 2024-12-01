from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from routes import plaid_blueprint
from cache import initialize_cache
from database import initialize_database
from swagger import templates

import config
import json

server = Flask(__name__)
server.debug = config.DEBUG
server.register_blueprint(plaid_blueprint, url_prefix='/plaid')
swagger = Swagger(server)

server.config['CACHE_TYPE'] = 'RedisCache'
server.config['CACHE_REDIS_HOST'] = config.REDIS_HOST
server.config['CACHE_REDIS_PORT'] = config.REDIS_PORT
initialize_cache(server)

server.config["MONGO_URI"] = config.MONGO_URI
initialize_database(server)

@server.route('/', methods=['GET'])
@swag_from(templates)
def get_root():
  result = { 'host': config.HOST, 'port': config.PORT }
  return jsonify(result)

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)