FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY /templates      /app/templates
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 8000
CMD [ "python", "app.py" ]
