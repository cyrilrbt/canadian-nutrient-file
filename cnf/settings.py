import os
import datetime
from urllib.parse import urljoin


ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = (os.getenv('CNF_DEBUG', 'True') == 'True')
TESTING = (os.getenv('CNF_TESTING', 'True') == 'True')
FLASK_DEBUG = DEBUG
FLASK_BIND = os.getenv('CNF_BIND', 'localhost')
FLASK_PORT = int(os.getenv('CNF_PORT', 8888))
ROOT_URL = 'http://' + FLASK_BIND + ':' + str(FLASK_PORT) + '/'

TEMPLATE_FOLDER = os.path.join(ROOT_PATH, 'cnf', 'templates')

MONGODB_HOST = os.getenv('CNF_MONGO_HOST', 'localhost')
MONGODB_PORT = int(os.getenv('CNF_MONGO_PORT', 27017))
MONGODB_DB = os.getenv('CNF_MONGO_DB', 'cnf')
