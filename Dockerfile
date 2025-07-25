FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

RUN mkdir -p /vol/web/media
RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user