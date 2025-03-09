# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /model

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY  app.py app.py
COPY  titanic_model.pkl titanic_model.pkl

#Exposing port 5000 from the container
EXPOSE 5000

#Starting the Python application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]