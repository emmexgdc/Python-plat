FROM python:3.12-alpine

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src /app

RUN addgroup -g 10001 -S app && adduser -u 10001 -S app -G app \
    && chown -R 10001:10001 /app

USER 10001

EXPOSE 5000

CMD ["python", "app.py"]
