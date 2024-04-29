from marshmallow import fields, validate

from extensions import ma
from models.medical_care import MedicalCare


class MedicalCareSchema(ma.SQLAlchemyAutoSchema):
    user_id = fields.Integer(required=True)
    name = fields.String(required=True, validate=validate.Length(min=5))
    birthdate = fields.Date(required=True)
    national_health_card_number = fields.Integer(required=True)
    cpf = fields.String(required=True)
    unit = fields.String(required=True)
    medical_care_date = fields.Date(required=True)
    health_condition = fields.String(required=True)

    class Meta:
        model = MedicalCare
        load_instance = True
        exclude = ["national_health_card_number", "cpf"]
