#!/bin/bash

python3 -m pytest tests.py --alluredir /results
allure  serve /results
