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

from openapi_client.models.service_docs_callflow_get_all import ServiceDocsCallflowGetAll

class TestServiceDocsCallflowGetAll(unittest.TestCase):
    """ServiceDocsCallflowGetAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCallflowGetAll:
        """Test ServiceDocsCallflowGetAll
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCallflowGetAll`
        """
        model = ServiceDocsCallflowGetAll()
        if include_optional:
            return ServiceDocsCallflowGetAll(
                data = openapi_client.models.service/callflow_output_short.service.CallflowOutputShort(
                    id = '', 
                    modules = [
                        ''
                        ], 
                    name = '', 
                    numbers = [
                        ''
                        ], 
                    patterns = [
                        ''
                        ], ),
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsCallflowGetAll(
        )
        """

    def testServiceDocsCallflowGetAll(self):
        """Test ServiceDocsCallflowGetAll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
