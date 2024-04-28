from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.resources.medical_care import MedicalCareList, MedicalCareItem

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(MedicalCareList, "/atendimentos")
api.add_resource(MedicalCareItem, "/atendimentos/<int:id>")


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
