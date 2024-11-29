import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('ENVIRONMENT')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT', '3101'))

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
DB_NAME = os.getenv('DB_NAME')
MONGO_URI = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{DB_NAME}'

PLAID_HOST = os.getenv('PLAID_HOST')  
PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
