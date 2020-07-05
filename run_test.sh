#!/bin/bash

#lsof -i tcp:4444

java -jar selenium-server-standalone.jar -role hub
java -jar selenium-server-standalone.jar -role webdriver -hub http://192.168.0.111:4444 \
      -browser browserName=chrome,platform=LINUX

python3 -m pytest tests.py --alluredir results
allure  serve /results
