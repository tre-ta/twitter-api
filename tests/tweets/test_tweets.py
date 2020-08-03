from unittest.mock import Mock, patch

import pytest
from src.tweets import Tweets

from tests.tweets import (
    INSERT_TWEETS_PARAMS,
    INSERT_TWEETS_TEST_CASES,
    MOST_FOLLOWED_PARAMS,
    MOST_FOLLOWED_TEST_CASES,
)


@pytest.mark.parametrize(INSERT_TWEETS_PARAMS, INSERT_TWEETS_TEST_CASES)
@patch("src.tweets.Tweets.__init__", return_value=None)
def test_insert_tweets(_, hashtags, expected_response):
    tweets = Tweets()
    tweets.database = Mock()
    tweets.database.save.return_value = 2
    response = tweets.insert_tweets(hashtags)
    assert response == expected_response


@pytest.mark.parametrize(MOST_FOLLOWED_PARAMS, MOST_FOLLOWED_TEST_CASES)
@patch("src.tweets.Tweets.__init__", return_value=None)
def test_get_most_followed_users(_, tweets_data, expected_response):
    tweets = Tweets()
    tweets.database = Mock()
    tweets.database.get_tweets.return_value = tweets_data
    response = tweets.get_most_followed_users()
    assert response == expected_response


@patch("src.tweets.Tweets.__init__", return_value=None)
def test_get_total_tweets_by_hashtag_lang(_):
    tweets = Tweets()
    tweets.database = Mock()
    tweets.database.tweets_collection.aggregate.return_value = ["1"]
    response = tweets.get_total_tweets_by_hashtag_lang()
    assert response == list(["1"])


@patch("src.tweets.Tweets.__init__", return_value=None)
def test_get_total_tweets_by_hour(_):
    tweets = Tweets()
    tweets.database = Mock()
    tweets.database.tweets_collection.aggregate.return_value = ["1"]
    response = tweets.get_total_tweets_by_hour()
    assert response == list(["1"])
