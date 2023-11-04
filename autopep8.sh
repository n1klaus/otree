#!/usr/bin/env bash
# Fix python scripts styling with autopep8 guidelines and pycodestyle style guide
VENV='./venv/*'

if [ ! "$(command -v autopep8)" ]
then
    echo "Missing package, start installing autopep8..."
    sudo python3 -m pip install pip --upgrade > /dev/null 2>&1 &&\
    sudo python3 -m pip install autopep8 -y > /dev/null 2>&1
fi

echo "Running autopep..."
find ./app/mini_ultimatum ./app/exit_survey -type f -name '*.py' ! -path '*/__pycache__/*' ! -path "$VENV" -exec \
    autopep8 --in-place --aggressive --recursive --verbose '{}' \;

if [ ! "$(command -v pycodestyle)" ]
then
    echo "Missing package, start installing pycodestyle..."
    sudo apt-get update -y > /dev/null 2>&1 &&\
    sudo apt-get install pycodestyle -y > /dev/null 2>&1
fi

echo -e "\n\nRunning pycodestyle..."
find ./app/mini_ultimatum ./app/exit_survey -type f -name '*.py' ! -path '*/__pycache__/*' ! -path "$VENV" -exec pycodestyle --verbose '{}' \;

echo -e "\nDone"
exit

