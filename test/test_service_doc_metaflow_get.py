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

from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet

class TestServiceDocMetaflowGet(unittest.TestCase):
    """ServiceDocMetaflowGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocMetaflowGet:
        """Test ServiceDocMetaflowGet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocMetaflowGet`
        """
        model = ServiceDocMetaflowGet()
        if include_optional:
            return ServiceDocMetaflowGet(
                data = openapi_client.models.service/metaflow_output.service.MetaflowOutput(
                    binding_digit = '', 
                    numbers = {
                        'key' : openapi_client.models.service/metaflow_pattern.service.MetaflowPattern(
                            children = {
                                'key' : openapi_client.models.service/metaflow_pattern.service.MetaflowPattern(
                                    data = { }, 
                                    module = 'transfer', )
                                }, 
                            data = { }, 
                            module = 'transfer', )
                        }, 
                    patterns = {
                        'key' : 
                        }, ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocMetaflowGet(
        )
        """

    def testServiceDocMetaflowGet(self):
        """Test ServiceDocMetaflowGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
