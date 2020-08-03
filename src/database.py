import os

from pymongo import MongoClient
from pymongo.errors import BulkWriteError


class Database:
    def __init__(self, logger):
        self.logger = logger
        self.__load_db()

    def __load_db(self):
        self.__set_envs()
        self.client = MongoClient(
            self.mongo_ip,
            self.mongo_port,
            username=self.mongo_username,
            password=self.mongo_password,
        )
        database = self.client.tweets_db
        self.tweets_collection = database.tweets_collection
        self.tweets_collection.create_index("id", unique=True)

    def __del__(self):
        self.client.close()

    def __set_envs(self):
        self.mongo_ip = os.environ.get("MONGO_IP", "127.0.0.1")
        self.mongo_port = os.environ.get("MONGO_PORT", 27017)
        self.mongo_username = os.environ.get("MONGO_USERNAME", "mongo")
        self.mongo_password = os.environ.get("MONGO_PASSWORD", "mongopw")

    def save(self, data):
        try:
            result = self.tweets_collection.insert_many(data, ordered=False)
            inserted_count = len(result.inserted_ids)
            return inserted_count
        except BulkWriteError as error:
            duplicated_amount = len(error.details["writeErrors"])
            inserted_count = error.details["nInserted"]
            self.logger.debug(error.details)
            self.logger.info(f"Duplicated documents: {duplicated_amount}")
            self.logger.info(f"Non-duplicated documents count: {inserted_count}")
            return inserted_count

    def get_tweets(self):
        return self.tweets_collection.find()
