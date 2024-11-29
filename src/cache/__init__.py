from flask_caching import Cache

cache = Cache()

def initialize_cache(server):
  try:
    cache.init_app(server)
  except Exception as e:
    server.logger.error(f'Error initializing redis cache: {e}')
    raise Exception(f'Failed to initialize redis cache: {e}')