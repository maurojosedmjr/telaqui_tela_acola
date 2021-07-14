SHELL := /bin/bash

black:
	black .

run-dev:
	export FLASK_APP=run.py && flask run

build:
	docker build -t telagogo .

run:
	docker run -it --rm --name telagogo -p 5000:5000 -d telagogo