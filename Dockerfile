ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim AS base

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD dbt run && python3 upload_to_s3.py