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

from openapi_client.models.service_call_queue_status_output import ServiceCallQueueStatusOutput

class TestServiceCallQueueStatusOutput(unittest.TestCase):
    """ServiceCallQueueStatusOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCallQueueStatusOutput:
        """Test ServiceCallQueueStatusOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCallQueueStatusOutput`
        """
        model = ServiceCallQueueStatusOutput()
        if include_optional:
            return ServiceCallQueueStatusOutput(
                active_recipient_count = 56,
                available_recipient_count = 56,
                node = '',
                stats = openapi_client.models.service/call_queue_status_stats.service.CallQueueStatusStats(
                    abandoned_sessions = 56, 
                    active_session_count = 56, 
                    average_wait = 56, 
                    estimated_wait = 56, 
                    longest_wait = 56, 
                    missed_sessions = 56, 
                    recipient_count = 56, 
                    total_sessions = 56, )
            )
        else:
            return ServiceCallQueueStatusOutput(
        )
        """

    def testServiceCallQueueStatusOutput(self):
        """Test ServiceCallQueueStatusOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
