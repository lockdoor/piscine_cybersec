run:
	docker run --rm \
	-p 8000:80 \
	-p 4242:22 \
	--name onion onion

vol:
	docker run --rm \
	-p 8000:80 \
	-v $(PWD)/hidden_service:/var/lib/tor/hidden_services \
	--name onion onion

build:
	cp ~/.ssh/id_rsa.pub .
	docker build -t onion .