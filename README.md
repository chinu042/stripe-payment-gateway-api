# Stripe Payment Gateway API

This repository contains a simple payment gateway API integration for Stripe.

## Defined Routes

- **/api/v1/create_intent**
  - **Description:** Create a payment intent.
  - **Method:** POST

- **/api/v1/capture_intent/ID**
  - **Description:** Capture a payment intent.
  - **Method:** POST

- **/api/v1/create_refund/ID**
  - **Description:** Create a refund for a payment.
  - **Method:** POST

- **/api/v1/get_intents**
  - **Description:** Retrieve payment intents.
  - **Method:** GET

## Usage

To use this API, you need to have a Stripe account and set up your API keys accordingly. Make sure to add your own API key and your Docker registry prefix in the Makefile.

## Makefile Commands

- **dev:** Installs required dependencies and runs the application locally.
- **image_build:** Builds the Docker image for the application.
- **container_run:** Runs a Docker container with the application.
- **build_run:** Builds the Docker image and runs the container.
- **image_push:** Pushes the Docker image to the specified registry.
- **build_push:** Builds the Docker image and pushes it to the registry.

Make sure to set the appropriate values for the following variables in the Makefile or at runtime:

- **TAG:** Docker image tag (defaults to 'latest').
- **PORT:** Port to run the application on (defaults to 5000).
- **REGISTRY_PREFIX:** Docker registry prefix.
- **STRIPE_API_KEY:** Stripe API key.

## Contribution

Feel free to contribute to this repository by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

