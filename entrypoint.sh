#!/bin/bash
./wait-for-it.sh -t 180 postgres_db:5432

python3 manage.py db migrate
python3 manage.py db upgrade
python3 entrypoint.py
