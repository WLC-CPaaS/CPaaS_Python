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

from openapi_client.models.service_docs_webhook_get_single import ServiceDocsWebhookGetSingle

class TestServiceDocsWebhookGetSingle(unittest.TestCase):
    """ServiceDocsWebhookGetSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsWebhookGetSingle:
        """Test ServiceDocsWebhookGetSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsWebhookGetSingle`
        """
        model = ServiceDocsWebhookGetSingle()
        if include_optional:
            return ServiceDocsWebhookGetSingle(
                data = openapi_client.models.model/account_webhook.model.AccountWebhook(
                    account_id = '', 
                    callback_method = '', 
                    callback_url = '', 
                    created_at = '', 
                    data = { }, 
                    id = '', 
                    is_active = True, 
                    title = '', 
                    updated_at = '', 
                    webhook_type = '', ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsWebhookGetSingle(
        )
        """

    def testServiceDocsWebhookGetSingle(self):
        """Test ServiceDocsWebhookGetSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
