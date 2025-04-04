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

from openapi_client.models.service_channel_run_metaflow_data import ServiceChannelRunMetaflowData

class TestServiceChannelRunMetaflowData(unittest.TestCase):
    """ServiceChannelRunMetaflowData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceChannelRunMetaflowData:
        """Test ServiceChannelRunMetaflowData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceChannelRunMetaflowData`
        """
        model = ServiceChannelRunMetaflowData()
        if include_optional:
            return ServiceChannelRunMetaflowData(
                children = {
                    'key' : openapi_client.models.service/channel_run_metaflow_data.service.ChannelRunMetaflowData(
                        children = {
                            'key' : openapi_client.models.service/channel_run_metaflow_data.service.ChannelRunMetaflowData(
                                data = { }, 
                                module = 'transfer', )
                            }, 
                        data = { }, 
                        module = 'transfer', )
                    },
                data = { },
                module = 'transfer'
            )
        else:
            return ServiceChannelRunMetaflowData(
                module = 'transfer',
        )
        """

    def testServiceChannelRunMetaflowData(self):
        """Test ServiceChannelRunMetaflowData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
