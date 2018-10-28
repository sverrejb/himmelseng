FROM python:3.6

WORKDIR app

COPY .   .
RUN pip install -r requirements.txt

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:80", "himmelseng:app" ]