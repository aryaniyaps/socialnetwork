#!/bin/sh
pipenv run alembic upgrade head
pipenv run uvicorn run app.asgi:application