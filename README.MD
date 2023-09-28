# Test Task
___

## Getting Started
___

1. Run server and db
    > docker-compose up

    All env variables will be copied from env.example

2. Apply migrations for create and fill db
    > docker exec -it test_task_api alembic upgrade head

3. Go to http://0.0.0.0:8000

## Built with
___
 - [Python 3.10](https://www.python.org/downloads/release/python-3100/): Python 3.10 is the newest major release of the Python programming language, and it contains many new features and optimizations.
 - [FastApi](https://fastapi.tiangolo.com/): The used framework.
 - [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using python type annotations.
 - [SQLAlchemy](https://www.sqlalchemy.org/): SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
 - [PostgreSQL](https://www.postgresql.org/): Database.
 - [Poetry](https://python-poetry.org/): Python packaging and dependency management made easy.
 - [Docker-compose](https://docs.docker.com/compose/): Compose is a tool for defining and running multi-container Docker applications.
