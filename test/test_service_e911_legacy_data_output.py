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

from openapi_client.models.service_e911_legacy_data_output import ServiceE911LegacyDataOutput

class TestServiceE911LegacyDataOutput(unittest.TestCase):
    """ServiceE911LegacyDataOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceE911LegacyDataOutput:
        """Test ServiceE911LegacyDataOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceE911LegacyDataOutput`
        """
        model = ServiceE911LegacyDataOutput()
        if include_optional:
            return ServiceE911LegacyDataOutput(
                house_number = '',
                predirectional = '',
                street_name = '',
                suite = ''
            )
        else:
            return ServiceE911LegacyDataOutput(
        )
        """

    def testServiceE911LegacyDataOutput(self):
        """Test ServiceE911LegacyDataOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
