# Setup
``` Bash
# Setup virtual environment
python3 -m venv .venv
# Activate virtual environment
source .venv/bin/activate
# Install otree
pip3 install -U otree
# Create project
otree startproject app
cd app
# Run server
otree devserver

# Create application
otree startapp mini_ultimatum
otree startapp exit_survey
```

# Testing the application locally
``` Bash
# Create virtual environment
python3 -m venv .venv
# Activate virtual environment
source .venv/bin/activate
# Change directory to app
cd app
# Install requirements
python3 -m pip install -U -r requirements.txt
# Run server
otree devserver
```
