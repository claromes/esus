from flask import request, jsonify
from flask_restful import Resource
import csv

from models.medical_care import MedicalCare


class MedicalCareList(Resource):

    def get(self):
        medical_care = MedicalCare.query.all()

        return jsonify(results=medical_care)
