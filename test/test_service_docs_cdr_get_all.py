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

from openapi_client.models.service_docs_cdr_get_all import ServiceDocsCdrGetAll

class TestServiceDocsCdrGetAll(unittest.TestCase):
    """ServiceDocsCdrGetAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCdrGetAll:
        """Test ServiceDocsCdrGetAll
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCdrGetAll`
        """
        model = ServiceDocsCdrGetAll()
        if include_optional:
            return ServiceDocsCdrGetAll(
                data = [
                    openapi_client.models.service/cdr_output_short.service.CdrOutputShort(
                        authorizing_id = '', 
                        billing_seconds = 56, 
                        bridge_id = '', 
                        call_id = '', 
                        call_priority = '', 
                        call_type = '', 
                        callee_id_name = '', 
                        callee_id_number = '', 
                        caller_id_name = '', 
                        caller_id_number = '', 
                        calling_from = '', 
                        cost = '', 
                        dialed_number = '', 
                        direction = '', 
                        duration_seconds = 56, 
                        from = '', 
                        hangup_cause = '', 
                        id = '', 
                        interaction_id = '', 
                        media_recordings = [
                            None
                            ], 
                        media_server = '', 
                        other_leg_call_id = '', 
                        owner_id = '', 
                        rate = '', 
                        rate_name = '', 
                        recording_url = '', 
                        request = '', 
                        timestamp = 56, 
                        timestamp_datetime = '', 
                        to = '', )
                    ],
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsCdrGetAll(
        )
        """

    def testServiceDocsCdrGetAll(self):
        """Test ServiceDocsCdrGetAll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
