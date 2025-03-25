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

from openapi_client.models.service_docs_call_queue_get_single_status import ServiceDocsCallQueueGetSingleStatus

class TestServiceDocsCallQueueGetSingleStatus(unittest.TestCase):
    """ServiceDocsCallQueueGetSingleStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocsCallQueueGetSingleStatus:
        """Test ServiceDocsCallQueueGetSingleStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocsCallQueueGetSingleStatus`
        """
        model = ServiceDocsCallQueueGetSingleStatus()
        if include_optional:
            return ServiceDocsCallQueueGetSingleStatus(
                data = openapi_client.models.service/call_queue_status_output.service.CallQueueStatusOutput(
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
                        total_sessions = 56, ), ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocsCallQueueGetSingleStatus(
        )
        """

    def testServiceDocsCallQueueGetSingleStatus(self):
        """Test ServiceDocsCallQueueGetSingleStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
