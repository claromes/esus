from flask import Blueprint
from flask_restful import Api

from api.resources.medical_care import MedicalCareList

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(MedicalCareList, "/atendimentos")
