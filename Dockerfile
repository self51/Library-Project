FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["python", "/app/library/manage.py", "migrate"]
CMD ["python", "/app/library/manage.py", "runserver", "0.0.0.0:8000"]