

FROM ubuntu:latest
FROM python:3.10
EXPOSE 8000
# set work directory
WORKDIR /home/wss
RUN ls
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]