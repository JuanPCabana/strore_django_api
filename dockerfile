FROM python:3.9.19-alpine3.19

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DB_NAME=store_db
ENV DB_USER=root
ENV DB_SECRET=root
ENV DB_HOST=54.167.246.98
ENV DB_PORT=3306
ENV DEBUG=True 


RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "store_project.wsgi:application"]