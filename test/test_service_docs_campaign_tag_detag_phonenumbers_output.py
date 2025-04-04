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

from openapi_client.models.service_docs_campaign_tag_detag_phonenumbers_output import ServiceDocsCampaignTagDetagPhonenumbersOutput

class TestServiceDocsCampaignTagDetagPhonenumbersOutput(unittest.TestCase):
    """ServiceDocsCampaignTagDetagPhonenumbersOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCampaignTagDetagPhonenumbersOutput:
        """Test ServiceDocsCampaignTagDetagPhonenumbersOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCampaignTagDetagPhonenumbersOutput`
        """
        model = ServiceDocsCampaignTagDetagPhonenumbersOutput()
        if include_optional:
            return ServiceDocsCampaignTagDetagPhonenumbersOutput(
                data = openapi_client.models.service/campaign_tag_detag_phonenumbers_output.service.CampaignTagDetagPhonenumbersOutput(
                    order_id = '', 
                    order_status = '', ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsCampaignTagDetagPhonenumbersOutput(
        )
        """

    def testServiceDocsCampaignTagDetagPhonenumbersOutput(self):
        """Test ServiceDocsCampaignTagDetagPhonenumbersOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
