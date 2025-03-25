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

from openapi_client.models.service_voicemail_message_output import ServiceVoicemailMessageOutput

class TestServiceVoicemailMessageOutput(unittest.TestCase):
    """ServiceVoicemailMessageOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceVoicemailMessageOutput:
        """Test ServiceVoicemailMessageOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceVoicemailMessageOutput`
        """
        model = ServiceVoicemailMessageOutput()
        if include_optional:
            return ServiceVoicemailMessageOutput(
                call_id = '',
                caller_id_name = '',
                caller_id_number = '',
                folder = '',
                var_from = '',
                length = 56,
                media_id = '',
                succeeded = [
                    ''
                    ],
                timestamp = 56,
                to = ''
            )
        else:
            return ServiceVoicemailMessageOutput(
        )
        """

    def testServiceVoicemailMessageOutput(self):
        """Test ServiceVoicemailMessageOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
