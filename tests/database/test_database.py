from unittest.mock import call, Mock, patch

import pytest
from src.database import Database
from pymongo.errors import BulkWriteError

from tests.database import (
    SAVE_EXCEPT_PARAMS,
    SAVE_EXCEPT_TEST_CASES,
    SAVE_PARAMS,
    SAVE_TEST_CASES,
)


def insert_many_factory(result):
    def insert_many_side_effect(*argc, **kwargs):
        raise result

    return insert_many_side_effect


@pytest.mark.parametrize(SAVE_EXCEPT_PARAMS, SAVE_EXCEPT_TEST_CASES)
@patch("src.database.Database.__init__", return_value=None)
def test_save_except(_, data, result, expected_result, details, info_1, info_2):
    database = Database()

    database.logger = Mock()

    database.tweets_collection = Mock(
        insert_many=Mock(side_effect=insert_many_factory(result))
    )

    inserted_count = database.save(data)

    assert inserted_count == expected_result
    database.logger.info.assert_has_calls([call(info_1), call(info_2)])


@pytest.mark.parametrize(SAVE_PARAMS, SAVE_TEST_CASES)
@patch("src.database.Database.__init__", return_value=None)
def test_save(_, data, result, expected_result):
    database = Database()
    database.tweets_collection = Mock(insert_many=Mock(return_value=result))

    inserted_count = database.save(data)
    assert inserted_count == expected_result


@patch("src.database.Database.__init__", return_value=None)
def test_get_tweets(_):
    database = Database()
    database.tweets_collection = Mock(find=Mock(return_value=["1"]))
    response = database.get_tweets()
    assert database.tweets_collection.find.return_value == response
