FROM python:3

COPY . .
RUN pip install -r requirements.txt

RUN nose2 -v

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "himmelseng:app" ]