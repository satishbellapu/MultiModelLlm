#!/bin/bash

# Delete the existing virtual environment if it exists
# if [ -d "venv" ]; then
#     rm -rf venv
#     echo "Existing virtual environment deleted."
# fi

# # Install the latest version of Python
# sudo apt-get update
# sudo apt-get install -y python3 python3-venv python3-pip

# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
# pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Virtual environment created, activated, and dependencies installed."

# Launch the Flask application
python3 app.py
