FROM python:alpine as builder

WORKDIR /app

RUN addgroup -S  app && adduser -S chintu 

RUN chown chintu:app /app

USER chintu  

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --target /app/packages

FROM gcr.io/distroless/python3 as deployer

WORKDIR /app

COPY --from=builder /app/packages /app/packages

ENV PYTHONPATH=/app/packages

COPY . .

CMD ["app.py"]


