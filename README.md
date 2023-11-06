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

# Create application
otree startapp mini_ultimatum
otree startapp exit_survey

# Run server
otree devserver
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

# Setup Docker container with Alpine Linux and Python
``` Bash
# Building the image using Dockerfile
docker build -f Dockerfile . --tag otree_image

docker run -it --rm \
    --name otree_container \
    --publish 8000:8000 \
    -d otree_image

docker exec -it otree_container bash
```

# References
- [oTree Documentation](https://otree.readthedocs.io/en/latest/index.html)
- [oTree Tutorial](https://otreecb.netlify.app/intro.html)
