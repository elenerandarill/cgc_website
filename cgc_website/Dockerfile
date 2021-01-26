FROM python:3.7-alpine
RUN apk add -U \
	bash \
	gcc \
	jpeg-dev \
	libc-dev \
	linux-headers \
	musl-dev \
	openjpeg-dev \
	zlib-dev \
  && rm -rf /var/cache/apk/*
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0:8000"]
RUN python manage.py collectstatic \
	&& python manage.py makemigrations
ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
