# Another project management software
# Copyright (C) 2021 Salah OSFOR <osfor.salah@gmail.com>

FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/
