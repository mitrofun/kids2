PROJECT_DIR=$(shell pwd)
VENV_DIR?=$(PROJECT_DIR)/.env
PIP?=$(VENV_DIR)/bin/pip
PYTHON?=$(VENV_DIR)/bin/python
NOSE?=$(VENV_DIR)/bin/nosetests

.PHONY: all clean test run requirements install virtualenv bower_install copy_settings

all: bower_install copy_settings virtualenv install create_database create_admin

bower_install:
	bower install

copy_settings:
	cp $(PROJECT_DIR)/src/settings/local.py.skeleton $(PROJECT_DIR)/src/settings/local.py
virtualenv:
	virtualenv -p python3 $(VENV_DIR) --no-site-packages

install: requirements

requirements:
	$(PIP) install -r $(PROJECT_DIR)/requirements/development.txt

loaddata:
	$(PYTHON) manage.py loaddata db.json;

create_database:
	$(PYTHON) manage.py migrate --noinput

create_admin:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@site.com', 'admin')" | $(PYTHON) manage.py shell

run:
	$(PYTHON) manage.py runserver localhost:8000

migrations:
	$(PYTHON) manage.py makemigrations

migrate:
	$(PYTHON) manage.py migrate

collect:
	$(PYTHON) manage.py collectstatic

shell:
	$(PYTHON) manage.py shell

test:
	$(PYTHON) manage.py test src/apps --verbosity=1 --logging-level=ERROR

clean_temp:
	find . -name '*.pyc' -delete
	rm -rf .coverage dist docs/_build htmlcov MANIFEST
	rm -rf media/

clean_db:
	find . -name '*.sqlite3' -delete

clean_venv:
	rm -rf $(VENV_DIR)

clean: clean_temp clean_venv clean_db