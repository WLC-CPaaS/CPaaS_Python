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

from openapi_client.models.models_device_output_full_sip import ModelsDeviceOutputFullSIP

class TestModelsDeviceOutputFullSIP(unittest.TestCase):
    """ModelsDeviceOutputFullSIP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelsDeviceOutputFullSIP:
        """Test ModelsDeviceOutputFullSIP
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelsDeviceOutputFullSIP`
        """
        model = ModelsDeviceOutputFullSIP()
        if include_optional:
            return ModelsDeviceOutputFullSIP(
                invite_format = '',
                password = '',
                username = ''
            )
        else:
            return ModelsDeviceOutputFullSIP(
        )
        """

    def testModelsDeviceOutputFullSIP(self):
        """Test ModelsDeviceOutputFullSIP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
