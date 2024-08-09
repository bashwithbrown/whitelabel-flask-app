#!/bin/bash

cd ..
source venv/bin/activate
export FLASK_APP=website
export FLASK_DEBUG=1
cd website

if [[ "$#" -eq 0 ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
elif [[ "$1" == "-d" ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app &
else
    echo "Invalid option: $1"
    echo "Usage: ./run.sh [-d]"
fi
