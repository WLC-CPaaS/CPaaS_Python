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

from openapi_client.models.service_docs_media_get_all import ServiceDocsMediaGetAll

class TestServiceDocsMediaGetAll(unittest.TestCase):
    """ServiceDocsMediaGetAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsMediaGetAll:
        """Test ServiceDocsMediaGetAll
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsMediaGetAll`
        """
        model = ServiceDocsMediaGetAll()
        if include_optional:
            return ServiceDocsMediaGetAll(
                data = [
                    openapi_client.models.service/media_output_short.service.MediaOutputShort(
                        id = '', 
                        is_prompt = True, 
                        language = '', 
                        media_source = '', 
                        name = '', )
                    ],
                next_start_key = '',
                page_size = 56,
                request_id = '',
                start_key = '',
                status_code = 56
            )
        else:
            return ServiceDocsMediaGetAll(
        )
        """

    def testServiceDocsMediaGetAll(self):
        """Test ServiceDocsMediaGetAll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
