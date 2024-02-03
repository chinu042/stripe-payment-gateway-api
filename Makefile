TAG?=latest
PORT?=5000
REGISTRY_PREFIX?=
STRIPE_API_KEY?=

dev:
	pip install -r requirements.txt
	export STRIPE_API_KEY=${STRIPE_API_KEY} && \
	python3 app.py

image_build:
	docker build -f Dockerfile -t ${REGISTRY_PREFIX}/stripe_payment_gateway_api:$(TAG) .

container_run:
	docker run -p ${PORT}:5000 -e STRIPE_API_KEY=${STRIPE_API_KEY} ${REGISTRY_PREFIX}/stripe_payment_gateway_api:$(TAG)

build_run:
	make image_build
	make container_run

image_push:
	docker push ${REGISTRY_PREFIX}/stripe_payment_gateway_api:$(TAG)

build_push:
	make image_build
	make image_push


