FROM python:3.10.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]