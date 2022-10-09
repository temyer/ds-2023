#!/bin/bash

set -exo pipefail

python3 -m doctest -o NORMALIZE_WHITESPACE -o ELLIPSIS -v morse.py > result.txt
