ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim AS base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .
