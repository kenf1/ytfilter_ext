FROM python:3.13.7-slim

RUN apt-get update && apt-get install -y \
	curl git neovim make\
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip

COPY ./setup/dev_requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt