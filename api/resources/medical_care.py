from flask import request
from flask_restful import Resource

from models.medical_care import MedicalCare
from api.schemas.medical_care import MedicalCareSchema
from extensions import db


class MedicalCareList(Resource):

    def get(self):
        medical_care_query = MedicalCare.query
        schema = MedicalCareSchema(many=True)

        date_filter = request.args.get("data_atendimento")
        health_condition_filter = request.args.get("condicao_saude")
        unit_filter = request.args.get("unidade")

        if date_filter:
            medical_care_query = medical_care_query.filter(
                MedicalCare.medical_care_date == date_filter)
        if health_condition_filter:
            if health_condition_filter == "hipertensao":
                medical_care_query = medical_care_query.filter(
                    MedicalCare.health_condition == "hipertensao")
            elif health_condition_filter == "diabetes":
                medical_care_query = medical_care_query.filter(
                    MedicalCare.health_condition == "diabetes")
            elif health_condition_filter == "ferida_vascular":
                medical_care_query = medical_care_query.filter(
                    MedicalCare.health_condition == "ferida vascular")
            elif health_condition_filter == "dengue":
                medical_care_query = medical_care_query.filter(
                    MedicalCare.health_condition == "dengue")
            elif health_condition_filter == "tuberculose":
                medical_care_query = medical_care_query.filter(
                    MedicalCare.health_condition == "tuberculose")
        if unit_filter:
            medical_care_query = medical_care_query.filter(
                MedicalCare.unit == unit_filter)

        medical_care = medical_care_query.all()

        return {"results": schema.dump(medical_care)}

    def post(self):
        schema = MedicalCareSchema()
        data = schema.load(request.json)

        medical_care = MedicalCare(**data)

        db.session.add(medical_care)
        db.session.commit()

        return {
            "message": "Atendimento criado.",
            "result": schema.dump(medical_care)
        }
