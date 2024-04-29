from flask import request
from flask_restful import Resource

from models.medical_care import MedicalCare
from api.schemas.medical_care import MedicalCareSchema
from extensions import db


class MedicalCareList(Resource):

    def get(self):
        schema = MedicalCareSchema(many=True)

        medical_care_query = MedicalCare.query

        date_filter = request.args.get("data_atendimento")
        health_condition_filter = request.args.get("condicao_saude")
        unit_filter = request.args.get("unidade")
        order_by = request.args.get("order_by")

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
        if order_by:
            for item in order_by.split(","):
                attr = getattr(MedicalCare, item)
                medical_care_query = medical_care_query.order_by(attr)

        medical_care = medical_care_query.all()

        return {"results": schema.dump(medical_care)}

    def post(self):
        schema = MedicalCareSchema()

        medical_care = MedicalCare(
            user_id=request.json["user_id"],
            name=request.json["name"],
            birthdate=request.json["birthdate"],
            national_health_card_number=request.
            json["national_health_card_number"],
            cpf=request.json["cpf"],
            unit=request.json["unit"],
            medical_care_date=request.json["medical_care_date"],
            health_condition=request.json["health_condition"])

        db.session.add(medical_care)
        db.session.commit()

        return {
            "message": "Atendimento criado.",
            "result": schema.dump(medical_care)
        }


class MedicalCareItem(Resource):

    def get(self, id):
        schema = MedicalCareSchema()

        medical_care = MedicalCare.query.get_or_404(id)

        return {"Atendimento": schema.dump(medical_care)}

    def patch(self, id):
        schema = MedicalCareSchema(partial=True)

        medical_care = MedicalCare.query.get_or_404(id)
        medical_care = schema.load(request.json, instance=medical_care)

        db.session.add(medical_care)
        db.session.commit()

        return {
            "message": "Atendimento atualizado.",
            "Atendimento": schema.dump(medical_care)
        }

    def delete(self, id):
        medical_care = MedicalCare.query.get_or_404(id)

        db.session.delete(medical_care)
        db.session.commit()

        return {"message": "Atendimento deletado."}
