from flask import Flask, jsonify, request
from flasgger import Swagger
from routes import plaid_blueprint
from cache import initialize_cache
from database import initialize_database

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
def get_root():
  """Root endpoint
    ---
    responses:
      200:
        description: An object displaying the hostname and port
  """
  result = { 'host': config.HOST, 'port': config.PORT }
  return jsonify(result)

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)