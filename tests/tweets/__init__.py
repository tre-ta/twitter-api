INSERT_TWEETS_PARAMS = ("hashtags", "expected_response")
INSERT_TWEETS_TEST_CASES = [
    (["sre"], f"Inserted 2 non-duplicated documents into the database."),
    ([], f"Inserted 0 non-duplicated documents into the database."),
    (["sre", "devops"], f"Inserted 4 non-duplicated documents into the database.")
]

MOST_FOLLOWED_PARAMS = ("tweets_data", "expected_response")
MOST_FOLLOWED_TEST_CASES = [
    (
        [
            {
                "id": "AkwyZ.remediation123.remediation",
                "created_at": "somedate123",
                "text": "remediation123",
                "user_id": 19485870,
                "user_name": "Antonio Vieira Santos",
                "user_screen_name": "AkwyZ",
                "hashtag": "remediation",
                "user_location": "Cork, London, Lisbon, Munich",
                "user_language": "en",
                "user_followers_count": 77839,
            },
            {
                "id": "marshawright.RealOpenBanking.openbanking",
                "created_at": "somedate",
                "text": "RealOpenBanking",
                "user_id": 61608747,
                "user_name": "Real Marsha Wright® | #StaySafe www.PromoNation.co",
                "user_screen_name": "marshawright",
                "hashtag": "openbanking",
                "user_location": "USA|EUROPE|ASIA|GLOBAL✈️",
                "user_language": "en",
                "user_followers_count": 546732,
            },
            {
                "id": "KirkDBorne.microservices123.microservices",
                "created_at": "somedate",
                "text": "microservices123",
                "user_id": 534563976,
                "user_name": "Kirk Borne",
                "user_screen_name": "KirkDBorne",
                "hashtag": "microservices",
                "user_location": "Maryland, USA",
                "user_language": "en",
                "user_followers_count": 264590,
            },
            {
                "id": "OttLegalRebeles.openbankingmock123.openbanking",
                "created_at": "somedate",
                "text": "openbankingmock123",
                "user_id": 1605693206,
                "user_name": "Marc R Gagné MAPP 🍁",
                "user_screen_name": "OttLegalRebels",
                "hashtag": "openbanking",
                "user_location": "Ottawa, Ontario",
                "user_language": "en",
                "user_followers_count": 73371,
            },
            {
                "id": "PRNews.metricsmock123.metrics",
                "created_at": "somedate",
                "text": "metricsmock123",
                "user_id": 26258900,
                "user_name": "PRNEWS",
                "user_screen_name": "PRNews",
                "hashtag": "metrics",
                "user_location": "US",
                "user_language": "en",
                "user_followers_count": 183292,
            }
        ],
        [
            (
                546732,
                {
                    "user_id": 61608747,
                    "user_name": "Real Marsha Wright® | #StaySafe www.PromoNation.co",
                    "user_screen_name": "marshawright",
                    "hashtag": "openbanking",
                    "user_location": "USA|EUROPE|ASIA|GLOBAL✈️",
                    "user_language": "en",
                    "user_followers_count": 546732,
                },
            ),
            (
                264590,
                {
                    "user_id": 534563976,
                    "user_name": "Kirk Borne",
                    "user_screen_name": "KirkDBorne",
                    "hashtag": "microservices",
                    "user_location": "Maryland, USA",
                    "user_language": "en",
                    "user_followers_count": 264590,
                },
            ),
            (
                183292,
                {
                    "user_id": 26258900,
                    "user_name": "PRNEWS",
                    "user_screen_name": "PRNews",
                    "hashtag": "metrics",
                    "user_location": "US",
                    "user_language": "en",
                    "user_followers_count": 183292,
                },
            ),
            (
                77839,
                {
                    "user_id": 19485870,
                    "user_name": "Antonio Vieira Santos",
                    "user_screen_name": "AkwyZ",
                    "hashtag": "remediation",
                    "user_location": "Cork, London, Lisbon, Munich",
                    "user_language": "en",
                    "user_followers_count": 77839,
                },
            ),
            (
                73371,
                {
                    "user_id": 1605693206,
                    "user_name": "Marc R Gagné MAPP 🍁",
                    "user_screen_name": "OttLegalRebels",
                    "hashtag": "openbanking",
                    "user_location": "Ottawa, Ontario",
                    "user_language": "en",
                    "user_followers_count": 73371,
                }
            )
        ]
    ),
    ([], []),
    (
        [
            {
                "id": "KirkDBorne.microservices123.microservices",
                "created_at": "somedate",
                "text": "microservices123",
                "user_id": 534563976,
                "user_name": "Kirk Borne",
                "user_screen_name": "KirkDBorne",
                "hashtag": "microservices",
                "user_location": "Maryland, USA",
                "user_language": "en",
                "user_followers_count": 264590,
            },
            {
                "id": "OttLegalRebeles.openbankingmock123.openbanking",
                "created_at": "somedate",
                "text": "openbankingmock123",
                "user_id": 1605693206,
                "user_name": "Marc R Gagné MAPP 🍁",
                "user_screen_name": "OttLegalRebels",
                "hashtag": "openbanking",
                "user_location": "Ottawa, Ontario",
                "user_language": "en",
                "user_followers_count": 73371,
            },
        ],
        [
            (
                264590,
                {
                    "user_id": 534563976,
                    "user_name": "Kirk Borne",
                    "user_screen_name": "KirkDBorne",
                    "hashtag": "microservices",
                    "user_location": "Maryland, USA",
                    "user_language": "en",
                    "user_followers_count": 264590,
                },
            ),
            (
                73371,
                {
                    "user_id": 1605693206,
                    "user_name": "Marc R Gagné MAPP 🍁",
                    "user_screen_name": "OttLegalRebels",
                    "hashtag": "openbanking",
                    "user_location": "Ottawa, Ontario",
                    "user_language": "en",
                    "user_followers_count": 73371,
                }
            )
        ]
    )
]
