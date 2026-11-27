FROM python:3.14.5-slim

WORKDIR /Worker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Worker/ . 

CMD ["python3", "main.py"]
