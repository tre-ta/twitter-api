from pymongo.errors import BulkWriteError
from pymongo.results import InsertManyResult


SAVE_EXCEPT_PARAMS = (
    "data",
    "result",
    "expected_result",
    "details",
    "info_1",
    "info_2",
)
SAVE_EXCEPT_TEST_CASES = [
    (
        {
            "id": "opsmatters_uk.ThelatestupdateforBroadcomincludesDXNetOps202Netwo.opentracing"
        },
        BulkWriteError(
            {
                "writeErrors": [
                    {
                        "index": 0,
                        "code": 11000,
                        "keyPattern": {"id": 1},
                        "keyValue": {
                            "id": "opsmatters_uk.ThelatestupdateforBroadcomincludesDXNetOps202Netwo.opentracing"
                        },
                    }
                ],
                "writeConcernErrors": [],
                "nInserted": 0,
                "nUpserted": 0,
                "nMatched": 0,
                "nModified": 0,
                "nRemoved": 0,
                "upserted": [],
            },
        ),
        0,
        {
            "writeErrors": [
                {
                    "index": 0,
                    "code": 11000,
                    "keyPattern": {"id": 1},
                    "keyValue": {
                        "id": "opsmatters_uk.ThelatestupdateforBroadcomincludesDXNetOps202Netwo.opentracing"
                    },
                }
            ],
            "writeConcernErrors": [],
            "nInserted": 0,
            "nUpserted": 0,
            "nMatched": 0,
            "nModified": 0,
            "nRemoved": 0,
            "upserted": [],
        },
        f"Duplicated documents: 1",
        f"Non-duplicated documents count: 0",
    )
]


SAVE_PARAMS = ("data", "result", "expected_result")
SAVE_TEST_CASES = [
    (
        [
            {
                "id": "opsmatters_uk.ThelatestupdateforBroadcomincludesDXNetOps202Netwo.opentracing"
            }
        ],
        InsertManyResult(
            [
                "opsmatters_uk.ThelatestupdateforBroadcomincludesDXNetOps202Netwo.opentracing"
            ],
            True,
        ),
        1,
    ),
    ([], InsertManyResult([], True), 0),
]
