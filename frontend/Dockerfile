
FROM node:lts-alpine

RUN npm i -g serve

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app

COPY . .

COPY package.json .
COPY package-lock.json .
RUN npm install

RUN npm run build

CMD ["npm", "run", "serve"]