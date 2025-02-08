run:
	docker run --rm \
	-p 8000:80 \
	-p 4243:4242 \
	--name onion onion

volume:
	docker run --rm \
	-p 8000:80 \
	-p 4243:4242 \
	-v $(PWD)/html:/var/www/html \
	-v $(PWD)/nginx.conf:/etc/nginx/sites-available/default \
	--name onion onion

build:
	mkdir -p .ssh
	cp ~/.ssh/id_rsa.pub .ssh
	docker build -t onion .