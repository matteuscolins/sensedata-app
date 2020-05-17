FROM python:3.6

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["flask", "run"]

EXPOSE 5000