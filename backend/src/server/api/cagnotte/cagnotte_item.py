import logging

from flask import jsonify, abort
from flask_restx import Resource
from db.models import Movement
from common.db.base import Database
from common.db.tools import to_dict, serialize
from webargs import fields
from webargs.flaskparser import use_args
from . import ns


LOG = logging.getLogger(__name__)

login_post = {
    "value": fields.Integer(required=True)
}


@ns.route('/cagnoting/')
class CagnotteItem(Resource):
    @use_args(login_post)
    def post(self, params):
        if not params:
            abort(415)

        with Database(auto_commit=True) as db:
            movement = Movement(params.get('value', False))
            db.add(movement)
            db.commit()
            return jsonify(serialize(to_dict(movement)))

    def get(self):
        with Database(auto_commit=True) as db:
            movements = db.query(Movement)
            sumx = 0
            for m in movements:
                sumx = sumx + m.value
            return jsonify(sum=sumx)
