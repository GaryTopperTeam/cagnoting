# from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from server.auth import Auth
from config.settings import SETTINGS


db = SQLAlchemy()
cors = CORS()
auth = Auth(server_url=SETTINGS['AUTH_API_URL'],
            client_id=SETTINGS['AUTH_API_CLIENT_ID'],
            realm_name="aioconnect")
# rest_api = swagger.docs(Api(), apiVersion='0.1')
