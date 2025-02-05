NAME = spider

all:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirement.txt

clean:
	rm -rf data
	rm -rf .venv

test: all
	. .venv/bin/activate && python3 ${NAME}.py https://www.42bangkok.com
