FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

COPY ./app /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
