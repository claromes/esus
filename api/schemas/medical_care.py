from extensions import ma
from models.medical_care import MedicalCare


class MedicalCareSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = MedicalCare
