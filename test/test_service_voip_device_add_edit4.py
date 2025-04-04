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

from openapi_client.models.service_voip_device_add_edit4 import ServiceVOIPDeviceAddEdit4

class TestServiceVOIPDeviceAddEdit4(unittest.TestCase):
    """ServiceVOIPDeviceAddEdit4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceVOIPDeviceAddEdit4:
        """Test ServiceVOIPDeviceAddEdit4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceVOIPDeviceAddEdit4`
        """
        model = ServiceVOIPDeviceAddEdit4()
        if include_optional:
            return ServiceVOIPDeviceAddEdit4(
                number = ''
            )
        else:
            return ServiceVOIPDeviceAddEdit4(
        )
        """

    def testServiceVOIPDeviceAddEdit4(self):
        """Test ServiceVOIPDeviceAddEdit4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
