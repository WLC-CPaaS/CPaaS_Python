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

from openapi_client.models.service_call_recording_parameters import ServiceCallRecordingParameters

class TestServiceCallRecordingParameters(unittest.TestCase):
    """ServiceCallRecordingParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCallRecordingParameters:
        """Test ServiceCallRecordingParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCallRecordingParameters`
        """
        model = ServiceCallRecordingParameters()
        if include_optional:
            return ServiceCallRecordingParameters(
                enabled = True,
                format = 'mp3',
                record_min_sec = 56,
                record_on_answer = True,
                record_on_bridge = True,
                record_sample_rate = 56,
                time_limit = 5,
                url = ''
            )
        else:
            return ServiceCallRecordingParameters(
        )
        """

    def testServiceCallRecordingParameters(self):
        """Test ServiceCallRecordingParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
