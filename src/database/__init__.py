from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_database(server):
  try:
    mongo.init_app(server)
  except Exception as e:
    server.logger.error(f'Error initializing mongodb: {e}')
    raise Exception(f'Failed to initialize mongodb: {e}')