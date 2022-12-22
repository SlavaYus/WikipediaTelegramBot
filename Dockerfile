FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram

RUN pip install asyncio

RUN pip install	wikipedia


COPY main.py /usr/src/app

