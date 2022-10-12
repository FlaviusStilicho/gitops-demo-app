FROM python:3.10-slim

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY /src/ /app/

EXPOSE 8080
WORKDIR /app/

ENTRYPOINT ["python", "main.py"]
