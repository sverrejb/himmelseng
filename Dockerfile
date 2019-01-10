# Frontend build image
FROM node as builder
WORKDIR /app
COPY package.json yarn.lock babel.config.js ./
COPY src src/
COPY public public/
RUN yarn install
RUN yarn build

# Production image
FROM tiangolo/uwsgi-nginx:python3.7
WORKDIR /hms
COPY --from=builder /app/dist dist
COPY . .
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN pip install -r requirements.txt
CMD ["./startup.sh"]