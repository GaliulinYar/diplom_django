FROM python:3.10

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .