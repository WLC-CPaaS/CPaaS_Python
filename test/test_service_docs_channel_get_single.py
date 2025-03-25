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

from openapi_client.models.service_docs_channel_get_single import ServiceDocsChannelGetSingle

class TestServiceDocsChannelGetSingle(unittest.TestCase):
    """ServiceDocsChannelGetSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsChannelGetSingle:
        """Test ServiceDocsChannelGetSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsChannelGetSingle`
        """
        model = ServiceDocsChannelGetSingle()
        if include_optional:
            return ServiceDocsChannelGetSingle(
                data = openapi_client.models.service/channel_output.service.ChannelOutput(
                    answered = True, 
                    authorizing_id = '', 
                    authorizing_type = '', 
                    callflow_id = '', 
                    channel_authorized = True, 
                    custom_application_vars = { }, 
                    custom_auth_headers = { }, 
                    custom_channel_vars = { }, 
                    custom_sip_headers = { }, 
                    destination = '', 
                    direction = '', 
                    elapsed_s = 56, 
                    from_tag = '', 
                    interaction_id = '', 
                    is_loopback = True, 
                    is_onhold = True, 
                    other_leg = '', 
                    owner_id = '', 
                    presence_id = '', 
                    request = '', 
                    reseller_id = '', 
                    timestamp = 56, 
                    to_tag = '', 
                    username = '', 
                    uuid = '', ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsChannelGetSingle(
        )
        """

    def testServiceDocsChannelGetSingle(self):
        """Test ServiceDocsChannelGetSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
