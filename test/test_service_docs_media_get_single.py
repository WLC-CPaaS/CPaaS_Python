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

from openapi_client.models.service_docs_media_get_single import ServiceDocsMediaGetSingle

class TestServiceDocsMediaGetSingle(unittest.TestCase):
    """ServiceDocsMediaGetSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsMediaGetSingle:
        """Test ServiceDocsMediaGetSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsMediaGetSingle`
        """
        model = ServiceDocsMediaGetSingle()
        if include_optional:
            return ServiceDocsMediaGetSingle(
                data = openapi_client.models.service/media_output_full.service.MediaOutputFull(
                    content_length = 56, 
                    content_type = '', 
                    description = '', 
                    id = '', 
                    language = '', 
                    media_source = '', 
                    name = '', 
                    streamable = True, 
                    tts = openapi_client.models.service/tts.service.TTS(
                        text = '', 
                        voice = 'female/en-US', ), ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsMediaGetSingle(
        )
        """

    def testServiceDocsMediaGetSingle(self):
        """Test ServiceDocsMediaGetSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
