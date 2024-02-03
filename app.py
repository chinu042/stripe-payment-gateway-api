from flask import Flask, jsonify, request
import os
import stripe

app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_API_KEY")

@app.route('/api/v1/create_intent', methods=['POST'])
def create_intent():
    try:
        data = request.json
        amount = data['amount']
        currency = data['currency']
        automatic_payment_methods = data.get('automatic_payment_methods')

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods=automatic_payment_methods
        )
        return jsonify({'clientSecret': payment_intent.client_secret})
    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 403


@app.route('/api/v1/capture_intent/<string:id>', methods=['POST'])
def capture_intent(id):
    try:
        payment_intent = stripe.PaymentIntent.capture(
            id
        )
        return jsonify({'paymentIntent': payment_intent})
    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 403


@app.route('/api/v1/create_refund/<string:id>', methods=['POST'])
def create_refund(id):
    try:
        refund = stripe.Refund.create(
            charge=id
        )
        return jsonify({'refund': refund})
    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 403


@app.route('/api/v1/get_intents/', methods=['GET'])
def get_intents():
    try:
        intents = stripe.PaymentIntent.list()
        return jsonify({'intents': [intent.to_dict() for intent in intents]})
    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 403


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
