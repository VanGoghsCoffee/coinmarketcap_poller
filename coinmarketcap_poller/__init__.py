import datetime
import requests


class Poller(object):
    def __init__(self, api_route, db):
        self.api_route = api_route
        self.db = db

    def run(self):
        data = []

        try:
            data = self._get_from_api()
        except ValueError as e:
            print(e)
        else:
            data = self._add_ts_to_data(data)

        if len(data) > 0:
            try:
                self._write_to_mongo(data)
            except ValueError as e:
                print(e)

    def _add_ts_to_data(self, data):
        data_with_ts = data
        ts = datetime.datetime.utcnow()
        for entry in data_with_ts:
            entry["ts"] = ts
        return data_with_ts

    def _get_from_api(self):
        response = requests.get(self.api_route)
        if response.status_code != 200:
            raise ValueError("No data received")
        return response.json()

    def _write_to_mongo(self, data):
        results = self.db.write_to_collection(data)
        if len(results.inserted_ids) < 1:
            raise ValueError("No data inserted")
        return results
