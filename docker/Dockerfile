FROM odoo:18.0

USER root

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    python3-dev \
    python3-venv \
    python3-wheel \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

# Copy custom modules
COPY ./addons /mnt/extra-addons

USER odoo