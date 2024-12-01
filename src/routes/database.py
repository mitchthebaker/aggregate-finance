from flask import Blueprint, request, jsonify
from flasgger import swag_from
from database import mongo
from swagger import templates

database_blueprint = Blueprint('db', __name__)

@db.route('/collections', method = ['GET'])
@swag_from(templates)
def collections():
  try:
        collections = mongo.db.list_collection_names()
        return jsonify({"collections": collections}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@db.route('/collections/<collection_name>', method = ['GET'])
@swag_from(templates)
def collection(collection_name):
  try:
        collections = mongo.db.list_collection_names()
        return jsonify({"collections": collections}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
