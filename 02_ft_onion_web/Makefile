run:
	docker run --rm \
	-p 8000:80 \
	-v $(PWD)/hidden_service:/var/lib/tor/hidden_services \
	--name onion onion

build:
	docker build -t onion .