import json
from flask import Flask, jsonify, request
from flasgger import Swagger
from routes import plaid_blueprint
from extensions import cache

import config

server = Flask(__name__)
server.debug = config.DEBUG
server.register_blueprint(plaid_blueprint, url_prefix='/plaid')
Swagger(server)

server.config['CACHE_TYPE'] = 'RedisCache'
server.config['CACHE_REDIS_HOST'] = config.REDIS_HOST
server.config['CACHE_REDIS_PORT'] = config.REDIS_PORT
cache.init_app(server)

@server.route('/', methods=['GET'])
def get_root():
  result = { 'host': config.HOST, 'port': config.PORT }
  return jsonify(result)

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)