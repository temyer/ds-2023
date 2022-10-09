#!/bin/bash

set -exo pipefail

python3 -m venv venv
source venv/bin/activate
pip install pytest

python3 -m pytest test_decode_pytest.py > result.txt