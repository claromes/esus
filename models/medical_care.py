from dataclasses import dataclass
from datetime import date

from extensions import db


@dataclass
class MedicalCare(db.Model):
    id: int
    name: str
    birthdate: date
    national_health_card_number: int
    cpf: int
    unit: str
    medical_care_date: date
    health_condition: str

    __tablename__ = "medical_care"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    national_health_card_number = db.Column(db.BigInteger,
                                            unique=True,
                                            nullable=False)
    cpf = db.Column(db.BigInteger, unique=True, nullable=False)
    unit = db.Column(db.String, nullable=False)
    medical_care_date = db.Column(db.Date, nullable=False)
    health_condition = db.Column(db.String, nullable=False)
