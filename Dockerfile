FROM node as builder
COPY . .
RUN yarn install
RUN yarn build

FROM tiangolo/uwsgi-nginx:python3.7

WORKDIR /hms

COPY --from=builder dist dist

COPY . .
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN pip install -r requirements.txt

#CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:80", "himmelseng:app" ]
#CMD [ "nginx", "-g", "daemon off;" ]
CMD ["./startup.sh"]