import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'templates.json')
with open(file_path, 'r') as json_file:
  templates = json.load(json_file)