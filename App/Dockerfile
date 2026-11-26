FROM python:3.14.5-slim

WORKDIR /App

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY App/ . 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "900"]