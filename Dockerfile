FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python3 app.py