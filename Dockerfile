FROM python:3.7


# install os Modules
RUN apt update -y && \
    apt install telnet && \
    rm -rf /var/lib/apt/lists/*
# Copy source code
RUN mkdir -p /data-copier
COPY app /data-copier/app
COPY requirements.txt /data-copier

# Install  Application dependencies
RUN pip install -r /data-copier/requirements.txt