from flask import request
from flask_restful import Resource
import csv


class MedicalCareList(Resource):

    def get(self):
        # Via CSV file
        csv_file = "atendimentos.csv"
        results = []

        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                results.append(row)

        return {"results": results}
