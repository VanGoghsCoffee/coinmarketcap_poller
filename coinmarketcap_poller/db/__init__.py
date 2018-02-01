from pymongo import MongoClient


class MongoDB(object):
    def __init__(self, client, db, collection):
        self.client = MongoClient(client)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def write_to_collection(self, data):
        return self.collection.insert_many(data)
