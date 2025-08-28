FROM ubuntu:latest

# Install default Python 3, pip, git, and venv
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Upgrade pip and install dependencies inside the venv
RUN /opt/venv/bin/pip install --upgrade pip PyYAML

# Copy feed.py and entrypoint.sh
COPY feed.py /usr/bin/feed.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Ensure Python and pip use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
