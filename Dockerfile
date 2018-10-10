FROM python:3

ADD himmelseng.py .
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD [ "python", "./himmelseng.py" ]