#!/bin/bash

set -exo pipefail

python3 -m unittest -v &> result.txt