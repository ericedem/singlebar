init:
	pip install -r requirements.txt

upgrade:
	pip install --upgrade -r requirements.txt

test:
	nosetests tests