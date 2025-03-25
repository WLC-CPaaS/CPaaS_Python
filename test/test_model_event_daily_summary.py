# coding: utf-8

"""
    White Label Communications CPaas API Documentation

    A CPaaS platform API

    The version of the OpenAPI document: 1.1
    Contact: support@whitelabelcomm.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.model_event_daily_summary import ModelEventDailySummary

class TestModelEventDailySummary(unittest.TestCase):
    """ModelEventDailySummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelEventDailySummary:
        """Test ModelEventDailySummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelEventDailySummary`
        """
        model = ModelEventDailySummary()
        if include_optional:
            return ModelEventDailySummary(
                account_id = '',
                component = '',
                created_at = '',
                transaction_count = 56,
                transaction_date = ''
            )
        else:
            return ModelEventDailySummary(
        )
        """

    def testModelEventDailySummary(self):
        """Test ModelEventDailySummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
