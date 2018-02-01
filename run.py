from apscheduler.schedulers.blocking import BlockingScheduler

from coinmarketcap_poller import Poller
from coinmarketcap_poller.db import MongoDB
from coinmarketcap_poller.config import MONGO_CLIENT, MONGO_COLLECTION, MONGO_DB


api_route = "https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=0"
db = MongoDB(MONGO_CLIENT, MONGO_COLLECTION, MONGO_DB)

poller = Poller(api_route, db)


def polling():
    poller.run()

scheduler = BlockingScheduler()
scheduler.add_job(polling, 'interval', minutes=1)
scheduler.start()
