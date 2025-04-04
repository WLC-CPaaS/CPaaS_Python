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

from openapi_client.models.service_docs_call_daily_summary import ServiceDocsCallDailySummary

class TestServiceDocsCallDailySummary(unittest.TestCase):
    """ServiceDocsCallDailySummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCallDailySummary:
        """Test ServiceDocsCallDailySummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCallDailySummary`
        """
        model = ServiceDocsCallDailySummary()
        if include_optional:
            return ServiceDocsCallDailySummary(
                data = [
                    openapi_client.models.model/call_daily_summary.model.CallDailySummary(
                        account_id = '', 
                        call_date = '', 
                        call_type = '', 
                        created_at = '', 
                        total_call_duration = '', )
                    ],
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsCallDailySummary(
        )
        """

    def testServiceDocsCallDailySummary(self):
        """Test ServiceDocsCallDailySummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
