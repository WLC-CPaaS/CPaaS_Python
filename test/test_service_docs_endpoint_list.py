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

from openapi_client.models.service_docs_endpoint_list import ServiceDocsEndpointList

class TestServiceDocsEndpointList(unittest.TestCase):
    """ServiceDocsEndpointList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsEndpointList:
        """Test ServiceDocsEndpointList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsEndpointList`
        """
        model = ServiceDocsEndpointList()
        if include_optional:
            return ServiceDocsEndpointList(
                data = [
                    openapi_client.models.model/endpoint_list.model.EndpointList(
                        created_at = '', 
                        endpoint_name = '', 
                        feature_name = '', 
                        id = 56, 
                        transaction_type = '', 
                        version = '', )
                    ],
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsEndpointList(
        )
        """

    def testServiceDocsEndpointList(self):
        """Test ServiceDocsEndpointList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
