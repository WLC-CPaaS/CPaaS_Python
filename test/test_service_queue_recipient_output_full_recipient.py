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

from openapi_client.models.service_queue_recipient_output_full_recipient import ServiceQueueRecipientOutputFullRecipient

class TestServiceQueueRecipientOutputFullRecipient(unittest.TestCase):
    """ServiceQueueRecipientOutputFullRecipient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceQueueRecipientOutputFullRecipient:
        """Test ServiceQueueRecipientOutputFullRecipient
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceQueueRecipientOutputFullRecipient`
        """
        model = ServiceQueueRecipientOutputFullRecipient()
        if include_optional:
            return ServiceQueueRecipientOutputFullRecipient(
                features = openapi_client.models.service/queue_recipient_output_full_features.service.QueueRecipientOutputFullFeatures(
                    account_upgrade = '', 
                    pro = True, )
            )
        else:
            return ServiceQueueRecipientOutputFullRecipient(
        )
        """

    def testServiceQueueRecipientOutputFullRecipient(self):
        """Test ServiceQueueRecipientOutputFullRecipient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
