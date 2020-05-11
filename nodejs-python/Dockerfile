FROM nikolaik/python-nodejs:python3.8-nodejs12-alpine

WORKDIR /usr/src

COPY package.json /usr/src

RUN npm install -q -g nodemon@2.0.3
RUN npm install -q -g serverless@1.70.0 
RUN npm install -q serverless-offline@6.1.5
RUN npm install -q serverless-offline-python@3.22.2

RUN npm install

COPY ./src/app/world/package.json /usr/src/app/world/package.json
RUN npm install --prefix /usr/src/app/world

COPY ./src/app/hello/requirements.txt /usr/src/app/hello/requirements.txt
RUN pip install -r /usr/src/app/hello/requirements.txt

COPY serverless.yml /usr/src
COPY ./src/app /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/app

EXPOSE 3000

# RUN python -m ptvsd --host 0.0.0.0 --port 5678 --multiprocess -c 'import src.hello.handler; print handler.hello()'