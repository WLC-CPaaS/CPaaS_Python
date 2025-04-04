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

from openapi_client.models.service_webhook_add import ServiceWebhookAdd

class TestServiceWebhookAdd(unittest.TestCase):
    """ServiceWebhookAdd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceWebhookAdd:
        """Test ServiceWebhookAdd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceWebhookAdd`
        """
        model = ServiceWebhookAdd()
        if include_optional:
            return ServiceWebhookAdd(
                callback_method = 'POST',
                callback_url = '',
                data = { },
                title = '012',
                webhook_type = ''
            )
        else:
            return ServiceWebhookAdd(
                callback_method = 'POST',
                callback_url = '',
                title = '012',
                webhook_type = '',
        )
        """

    def testServiceWebhookAdd(self):
        """Test ServiceWebhookAdd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
