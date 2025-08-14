#!/bin/bash

set -e

# 1) Create the virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# 2) Activate the virtual environment
source .venv/bin/activate

# 3) Install requirements
pip install -r requirements.txt

# 4) Run the script
python error.py
