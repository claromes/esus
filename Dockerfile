FROM python:3.10.14-slim

WORKDIR /api

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]
