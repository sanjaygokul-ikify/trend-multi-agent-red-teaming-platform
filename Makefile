build:	docker-compose build
test:	pytest tests --cov=.
doc:	pip install -r docs/requirements.txt && mkdocs build
lint:	mypy . && bandit -r .
release:	poetry build && poetry publish