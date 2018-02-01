FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py ./
COPY coinmarketcap_poller/ ./

CMD [ "python", "./run.py" ]