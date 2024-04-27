from extensions import db


class MedicalCare(db.Model):
    __tablename__ = "medical_care"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    national_health_card_number = db.Column(db.BigInteger, nullable=False)
    cpf = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False)
    medical_care_date = db.Column(db.Date, nullable=False)
    health_condition = db.Column(db.String, nullable=False)
