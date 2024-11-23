import json
from flask import Flask, jsonify, request

import config

server = Flask(__name__)
server.debug = config.DEBUG

@server.route('/', methods=['GET'])
def get_root():
  arr = ["endpoint works as expected"]
  return jsonify(arr)

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)