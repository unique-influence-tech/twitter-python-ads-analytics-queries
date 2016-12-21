import unittest

from mock import patch
from random import randint
from twitter_ads.enum import METRIC_GROUP, GRANULARITY


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.metric_groups = [
            METRIC_GROUP.BILLING,
            METRIC_GROUP.ENGAGEMENT,
            METRIC_GROUP.WEB_CONVERSION
        ]
        cls.granularity = GRANULARITY.DAY
        cls.response_dict = [{}]

if __name__ == "__main__":
    test_cases = []
    
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=5).run(suite)
