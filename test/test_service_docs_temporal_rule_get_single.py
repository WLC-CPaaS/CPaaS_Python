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

from openapi_client.models.service_docs_temporal_rule_get_single import ServiceDocsTemporalRuleGetSingle

class TestServiceDocsTemporalRuleGetSingle(unittest.TestCase):
    """ServiceDocsTemporalRuleGetSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsTemporalRuleGetSingle:
        """Test ServiceDocsTemporalRuleGetSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsTemporalRuleGetSingle`
        """
        model = ServiceDocsTemporalRuleGetSingle()
        if include_optional:
            return ServiceDocsTemporalRuleGetSingle(
                data = openapi_client.models.service/temporal_rule_output_full.service.TemporalRuleOutputFull(
                    cycle = '', 
                    days = [
                        56
                        ], 
                    enabled = True, 
                    id = '', 
                    interval = 56, 
                    month = 56, 
                    name = '', 
                    ordinal = '', 
                    start_date = 56, 
                    time_window_start = 56, 
                    time_window_stop = 56, 
                    wdays = [
                        ''
                        ], ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsTemporalRuleGetSingle(
        )
        """

    def testServiceDocsTemporalRuleGetSingle(self):
        """Test ServiceDocsTemporalRuleGetSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
