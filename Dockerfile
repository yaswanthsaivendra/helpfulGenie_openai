FROM python:3.12.1-slim-bookworm


# set work directory
WORKDIR /

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE=false 


# System deps:
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    libpq-dev \
    # Cleaning cache:
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && pip install "poetry==$POETRY_VERSION" && poetry --version


COPY pyproject.toml poetry.lock ./

# Install dependencies:
RUN poetry install

COPY . .