import logging
import os
import re
from datetime import datetime

import requests
from pymongo import MongoClient
from pymongo.errors import BulkWriteError

from src.database import Database


class Tweets:
    def __init__(self):
        self.logger = self.__get_logger()
        self.database = Database(self.logger)

    def __get_logger(self):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def insert_tweets(self, hashtags):
        urls = self.__get_urls(hashtags)
        bearer = self.__get_bearer()
        headers = {"Authorization": bearer}

        inserted_count = 0
        for url in urls:
            req = requests.get(url, headers=headers)
            hashtag = hashtags[urls.index(url)]
            filtered_data = self.__filter_json(req.json(), hashtag)
            saved_to_db = self.database.save(filtered_data)
            inserted_count = inserted_count + saved_to_db

        return f"Inserted {inserted_count} non-duplicated documents into the database."

    @staticmethod
    def __get_urls(hashtags):
        urls = []
        for item in hashtags:
            base_search_url = "https://api.twitter.com/1.1/search/tweets.json"
            filters = f"?q=%23{item}&result_type=recent&count=100&include_entities=true"
            urls.append(base_search_url + filters)
        return urls

    @staticmethod
    def __get_bearer():
        return "Bearer " + os.environ.get("BEARER_TOKEN")

    def __filter_json(self, data, hashtag):
        filtered_data = []

        for item in data["statuses"]:
            created_at = self.__filter_date(item["created_at"])
            id_ = self.__get_custom_id(item, hashtag)
            filtered_item = {
                "id": id_,
                "created_at": created_at,
                "hashtag": hashtag,
                "text": item["text"],
                "user_id": item["user"]["id"],
                "user_name": item["user"]["name"],
                "user_screen_name": item["user"]["screen_name"],
                "user_location": item["user"]["location"],
                "user_language": item["metadata"]["iso_language_code"],
                "user_followers_count": item["user"]["followers_count"],
            }
            filtered_data.append(filtered_item)

        return filtered_data

    @staticmethod
    def __filter_date(full_date):
        created_at = datetime.strptime(full_date, "%a %b %d %H:%M:%S +0000 %Y")
        # bringing it down to zero to only deal with hours
        created_at = created_at.replace(minute=0, second=0)
        return created_at

    @staticmethod
    def __get_custom_id(item, hashtag):
        user_screen_name = item["user"]["screen_name"]
        text = re.sub("[^A-Za-z0-9]+", "", item["text"])
        text = text[0:50] if len(text) >= 50 else text
        id_ = f"{user_screen_name}.{text}.{hashtag}"
        return id_

    def get_most_followed_users(self):
        tweets = self.database.get_tweets()
        user_followers_count = []

        for item in tweets:
            user = {
                "user_id": item["user_id"],
                "user_name": item["user_name"],
                "user_screen_name": item["user_screen_name"],
                "hashtag": item["hashtag"],
                "user_location": item["user_location"],
                "user_language": item["user_language"],
                "user_followers_count": item["user_followers_count"],
            }
            user_followers_count.append((item["user_followers_count"], user))

        users = sorted(user_followers_count, key=lambda item: item[0], reverse=True)
        return users[:5]

    def get_total_tweets_by_hashtag_lang(self):
        aggregation = [
            {
                "$group": {
                    "_id": {"hashtag": "$hashtag", "language": "$user_language"},
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1}},
        ]
        return list(self.database.tweets_collection.aggregate(aggregation))

    def get_total_tweets_by_hour(self):
        aggregation = [
            {
                "$group": {
                    "_id": {
                        "$concat": [{"$substr": [{"$hour": "$created_at"}, 0, 2]},]
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1}},
        ]
        return list(self.database.tweets_collection.aggregate(aggregation))
