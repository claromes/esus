# e-SUS API REST ![A Flask Project](assets/flask-project.png "A Flask Project")

Esta API REST fornece endpoints para gerenciar atendimentos médicos do sistema e-SUS, permitindo listar, inserir, atualizar e deletar dados.

É possível filtrar resultados por data de atendimento, condição de saúde do paciente e pela unidade de atendimento, além de ordenar os resultados. Os dados sensíveis dos pacientes (CPF e CNS) foram anonimizados.

## Dados

Os dados em CSV são inseridos no banco de dados usando a biblioteca `csvkit`.

O header do arquivo CSV foi alterado para se adaptar ao banco de dados e a primeira coluna foi deletada, para que o ID de cada atendimento médico seja criado automaticamente.

## Stack

**API**: Flask Framework

**Extensões Flask**: Flask-RESTful, Flask-SQLAlchemy (Legacy Query Interface) e Flask-Marshmallow

**Banco de Dados**: PostgreSQL

**ORM**: SQLAlchemy

**Schema**: marshmallow

**Containerização**: Docker

**Utilitário**: csvkit

## Endpoints

### Listar todos os atendimentos

Este endpoint retorna uma lista de todos os atendimentos registrados.

- Método: `GET`
- URL: `http://localhost:8001/api/v1/atendimentos?{query_params}`
- Filtros:

  Os filtros podem ser combinados entre si.

  - `data_atendimento` (str): Formato 'YYYY-mm-dd'.
  - `condicao_saude` (str): hipertensao|diabetes|ferida vascular|dengue|tuberculose.
  - `unidade` (str)

- Ordenação:

  A ordenação pode ser feita com multiplas opções separadas por vírgula.

  - `order_by` (str): id, user_id, name, birthdate, unit, medical_care_date, health_condition

**Exemplo**

```bash
curl http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=diabetes&order_by=user_id,medical_care_date`
```

### Listar um atendimento específico

Este endpoint retorna os detalhes de um atendimento específico com base no seu ID.

- Método: `GET`
- URL: `http://localhost:8001/api/v1/atendimentos/{id}`

**Exemplo**

```bash
curl http://localhost:8001/api/v1/atendimentos/1`
```

### Criar um atendimento

Este endpoint cria um novo atendimento com base nos dados enviados.

- Método: `POST`
- URL: `http://localhost:8001/api/v1/atendimentos`

**Exemplo**

```bash
curl -X POST \
 http://127.0.0.1:8001/api/v1/atendimentos \
 -H 'Content-Type: application/json' \
 -d '{
"user_id": 123,
"name": "John Doe",
"birthdate": "2000-01-01",
"national_health_card_number": 123456789,
"cpf": "123.456.789-10",
"unit": "Unidade 1",
"medical_care_date": "2024-04-28",
"health_condition": "dengue"
}'
```

### Atualizar um atendimento

Este endpoint atualiza as informações de um atendimento específico com base no seu ID.

- Método: `PATCH`
- URL: `http://localhost:8001/api/v1/atendimentos/{id}`

**Exemplo**

```bash
curl -X PATCH \
 http://127.0.0.1:8001/api/v1/atendimentos/1 \
 -H 'Content-Type: application/json' \
 -d '{
"name": "John D."
}'
```

### Deletar um atendimento

Este endpoint exclui um atendimento específico com base no seu ID.

- Método: `DELETE`
- URL: `http://localhost:8001/api/v1/atendimentos/{id}`

**Exemplo**

```bash
curl -X DELETE http://127.0.0.1:8001/api/v1/atendimentos/1
```

## Desenvolvimento

### Pré-requisitos

- Python 3.8 ou superior
- Docker Compose

### Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone git@github.com:claromes/esus.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd esus
   ```

3. Crie um ambiente virtual de Python:

   ```bash
   python -m venv .venv
   ```

   ```bash
   source .venv/bin/activate
   ```

4. Copie o arquivo `.env.example` e crie um arquivo `.env`:

   ```bash
   cp .env.example .env
   ```

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

1. Inicie o banco de dados PostgreSQL:

   ```bash
   docker compose up -d postgres_esus
   ```

2. Construa e inicie o servidor Flask:

   ```bash
   docker compose up --build flask_esus
   ```

3. Importe os dados iniciais para o banco de dados:

   Altere o hostname do banco de dados caso necessário.

   ```bash
   csvsql --db postgresql://postgres:postgres@localhost:5432/postgres --tables medical_care --insert --no-create atendimentos.csv
   ```

## Créditos

[Clarissa Mendes](https://claromes.com)
