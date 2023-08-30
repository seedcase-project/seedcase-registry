FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

RUN apk update; \
    apk add less openssh postgresql-dev gcc python3-dev musl-dev git npm

# copy requirement file fo docker build environment before pip install
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk add curl

COPY . .

ENTRYPOINT ["/home/app/entrypoint.sh"]