FROM python:3.8

ADD . .

RUN sh initialize.sh

EXPOSE 8000

CMD ["python3", "API/main.py"]
