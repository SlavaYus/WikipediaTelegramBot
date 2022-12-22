FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram

RUN pip install asyncio

RUN pip install	wikipedia

RUN pip install	re

RUN pip install	datatime

COPY main.py /usr/src/app

