#!/bin/bash

if [ -n "$1" ]; then
  pip install -r $1
fi

python /validate.py