FROM node:14-alpine3.11

WORKDIR /user/src

COPY package*.json ./
RUN npm install

COPY . .
EXPOSE 3000

CMD ["npm", "run", "start:dev"]