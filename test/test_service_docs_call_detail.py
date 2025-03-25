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

from openapi_client.models.service_docs_call_detail import ServiceDocsCallDetail

class TestServiceDocsCallDetail(unittest.TestCase):
    """ServiceDocsCallDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCallDetail:
        """Test ServiceDocsCallDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCallDetail`
        """
        model = ServiceDocsCallDetail()
        if include_optional:
            return ServiceDocsCallDetail(
                data = [
                    openapi_client.models.model/call_detail.model.CallDetail(
                        account_id = '', 
                        call_duration = '', 
                        call_id = '', 
                        call_time = '', 
                        call_type = '', 
                        callee_name = '', 
                        callee_number = '', 
                        caller_name = '', 
                        caller_number = '', 
                        created_at = '', )
                    ],
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsCallDetail(
        )
        """

    def testServiceDocsCallDetail(self):
        """Test ServiceDocsCallDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
