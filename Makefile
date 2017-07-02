.PHONY: all help run worker qa coupon social

# target: all - Default target. Does nothing.
all:
	@clear
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@clear
	@egrep "^# target:" [Mm]akefile

# target: run - Run django server
run:
	python3 manage.py runserver 0.0.0.0:8000

# target: worker - Run rq workers
worker:
	python3 manage.py rqworker default

# target: qa - Run pytest
qa:
	pytest
