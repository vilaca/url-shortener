FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["uwsgi","uwsgi.ini"]
