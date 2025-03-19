#!/bin/bash

# Create necessary directories
mkdir -p addons
mkdir -p logs

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up pre-commit hooks
pre-commit install

# Create docker volumes
docker volume create odoo-db-data
docker volume create odoo-web-data

echo "Setup completed successfully!"