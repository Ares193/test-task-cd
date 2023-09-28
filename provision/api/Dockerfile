FROM python:3.10.13-slim as builder
ENV POETRY_VERSION=1.5.1\
    PATH="/opt/venv/bin:$PATH"
COPY ./pyproject.toml ./poetry.lock* ./
RUN apt-get update && apt-get install -y git && \
    pip install "poetry==$POETRY_VERSION" && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    python -m venv /opt/venv
RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM python:3.10.13-slim
RUN apt-get -y clean
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    TZ=Europe/Moscow \
    PYTHONPATH=/app
COPY ./alembic.ini /app/alembic.ini
COPY ./pyproject.toml /app/pyproject.toml
COPY ./.env.example /app/.env
COPY ./app /app/app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
