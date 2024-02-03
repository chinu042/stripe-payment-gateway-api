FROM python:3.12.1-slim-bookworm

WORKDIR /stripe-payment-gateway-api

COPY requirements.txt /stripe-payment-gateway-api

RUN pip install -r requirements.txt

COPY app.py /stripe-payment-gateway-api

EXPOSE 5000

CMD ["python", "app.py"]