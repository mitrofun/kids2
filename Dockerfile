FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/public/
WORKDIR /code
COPY requirements.txt /code
COPY requirements /code/requirements
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install -r requirements/dev.txt
ADD . /code/
