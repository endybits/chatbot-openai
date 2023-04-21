import os
import json


path = 'core/config.json'

if not os.path.exists(path):
    raise Exception(f'The file config.json is missing!')

def get_config(filename: str = path):
    config = json.loads(open(filename, 'r').read())
    return config

cfg = get_config()
openai_apikey = cfg['api']['openai_apikey']