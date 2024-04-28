# e-SUS API REST

docker compose up -d postgres_esus

docker compose build

docker compose up flask_esus

csvsql --db postgresql://postgres:postgres@localhost:5432/postgres --tables medical_care --insert --no-create atendimentos.csv

curl -X POST \
 http://127.0.0.1:8001/api/v1/atendimentos \
 -H 'Content-Type: application/json' \
 -d '{
"user_id": 123,
"name": "User 1",
"birthdate": "2000-01-01",
"national_health_card_number": 123456789,
"cpf": "123.456.789-00",
"unit": "Unidade 1",
"medical_care_date": "2024-04-28",
"health_condition": "diabetes"
}'
