FROM python:3.13.7-slim

RUN python3 -m pip install --upgrade pip

COPY ./setup/mongo_prune_requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./mongo_prune ./mongo_prune

CMD ["python3", "mongo_prune/main.py"]