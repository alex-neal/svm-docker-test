FROM tiangolo/meinheld-gunicorn-flask:python3.7

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r ./requirements.txt

COPY main.py __init__.py /app/