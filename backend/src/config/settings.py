import os


SETTINGS = {}
SETTINGS['POSTGRES_HOST'] = os.environ['POSTGRES_HOST']
SETTINGS['POSTGRES_PORT'] = os.environ['POSTGRES_PORT']

SETTINGS['POSTGRES_USER'] = os.environ['POSTGRES_USER']
SETTINGS['POSTGRES_PASSWORD'] = os.environ['POSTGRES_PASSWORD']
SETTINGS['POSTGRES_DB'] = os.environ['POSTGRES_DB']
SETTINGS['DEBUG_MODE'] = bool(os.environ['DEBUG_MODE'])
