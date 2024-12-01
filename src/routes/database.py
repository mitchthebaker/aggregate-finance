from flask import Blueprint, request, jsonify
from flasgger import swag_from
from database import mongo
from swagger import templates

database_blueprint = Blueprint('db', __name__)

@database_blueprint.route('/collections', methods = ['GET'])
@swag_from(templates)
def collections():
  try:
    collections = mongo.db.list_collection_names()
    return jsonify({"collections": collections}), 200
  except Exception as e:
    return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@database_blueprint.route('/collections/<collection_name>', methods = ['GET'])
@swag_from(templates)
def collection(collection_name):
  try:
    collection = mongo.db[collection_name]
    if collection is None:
      return jsonify({ 'error': 'collection_name is required and must be a valid collection name' }), 400
    
    # Fetch query parameters for filtering and sorting
    category_filter = request.args.get('category')
    sort_by = request.args.get('sort_by', 'date')  # Default sort by 'date'
    sort_order = request.args.get('sort_order', 'desc')  # Default sort order is ascending

    query = {}
    if category_filter:
      query['category'] = category_filter
    
    sort_direction = 1 if sort_order == 'asc' else -1
    documents = list(collection.find(query).sort(sort_by, sort_direction))
    return jsonify({ 'documents': documents }), 200
  except Exception as e:
    return jsonify({"error": f"An error occurred: {str(e)}"}), 500
