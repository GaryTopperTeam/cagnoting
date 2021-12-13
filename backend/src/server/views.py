import logging
from flask import jsonify, Blueprint


LOG = logging.getLogger(__name__)

blueprint = Blueprint('views', __name__)

# rest_api.add_resource(Login, '/api/users/login', methods=['POST'])
# rest_api.add_resource(Signup, '/api/users/signup', methods=['POST'])
# rest_api.add_resource(AccountItem, '/api/accounts', methods=['PATCH'])


@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)
