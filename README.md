# e-SUS API REST

docker compose up -d postgres_esus

docker compose build

docker compose up flask_esus

csvsql --db postgresql://postgres:postgres@localhost:5432/postgres --tables medical_care --insert --no-create atendimentos.csv

curl -X POST \
 http://127.0.0.1:8001/api/v1/atendimentos \
 -H 'Content-Type: application/json' \
 -d '{
"user_id": 1285,
"name": "AA5 User 2",
"birthdate": "1997-01-01",
"national_health_card_number": 12112289,
"cpf": "123.333.229-00",
"unit": "Unidade 1",
"medical_care_date": "2024-04-28",
"health_condition": "diabetes"
}'

curl -X PUT \
 http://127.0.0.1:8001/api/v1/atendimentos/9337 \
 -H 'Content-Type: application/json' \
 -d '{
"name": "AA5 User 555"
}'

curl -X DELETE http://127.0.0.1:8001/api/v1/atendimentos/93
