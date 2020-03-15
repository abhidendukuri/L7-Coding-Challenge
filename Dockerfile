FROM python:3.7.0

COPY . /App

WORKDIR /App

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["App.py"]