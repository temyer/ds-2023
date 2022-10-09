#!/bin/bash

set -exo pipefail

python3 -m venv venv
source venv/bin/activate
pip install coverage


python -m coverage run -m unittest -v &> result.txt
python -m coverage html
