from unittest.mock import call, Mock, patch

from fastapi.testclient import TestClient
from src.api import api, tweets


client = TestClient(api)


@patch("src.api.tweets")
def test_insert_tweets(mocked_tweets):
    mocked_tweets.insert_tweets = Mock(return_value=["1"])
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["1"]


@patch("src.api.tweets")
def test_most_followed_users(mocked_tweets):
    mocked_tweets.get_most_followed_users = Mock(return_value=["1"])
    response = client.get("/most-followed-users")
    assert response.status_code == 200
    assert response.json() == ["1"]


@patch("src.api.tweets")
def test_total_hashtag_lang(mocked_tweets):
    mocked_tweets.get_total_tweets_by_hashtag_lang = Mock(return_value=["1"])
    response = client.get("/total-hashtag-lang")
    assert response.status_code == 200
    assert response.json() == ["1"]


@patch("src.api.tweets")
def test_total_per_hour(mocked_tweets):
    mocked_tweets.get_total_tweets_by_hour = Mock(return_value=["1"])
    response = client.get("/total-per-hour")
    assert response.status_code == 200
    assert response.json() == ["1"]


@patch("src.api.tweets")
def test_metrics(mocked_tweets):
    response = client.get("/metrics")
    assert response.status_code == 200
