#! /usr/bin/env bash

# Let the DB start
python /fastapi-project/src/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /fastapi-project/src/initial_data.py