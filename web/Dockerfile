FROM node:12-alpine as build

WORKDIR /web

COPY package.json /web/package.json

RUN npm install

COPY . /web

RUN npm run build