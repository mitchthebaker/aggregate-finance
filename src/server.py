import json
from flask import Flask, jsonify, request

server = Flask(__name__)

@server.route('/', methods=['GET'])
def get_root():
  arr = ["endpoint works as expected"]
  return jsonify(arr)

if __name__ == '__main__':
  server.run(port=3101)