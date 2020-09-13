lint:
	black lib && \
	black tests && \
	pylint lib

test:
	pytest -vv

install-dev:
	pip install -r requirements-dev.txt

install:
	pip install -r requirements.txt