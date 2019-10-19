FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app
COPY . /app
#RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["gunicorn", "mgmtApp.wsgi:application", "--bind", "0.0.0.0:8000"]