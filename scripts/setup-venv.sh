#!/bin/bash

cd ..

python3.11 -m venv venv
source venv/bin/activate
python -m pip install -U pip

cd website

python -m pip install -r requirements.txt