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

from openapi_client.models.service_device_output_full_media import ServiceDeviceOutputFullMedia

class TestServiceDeviceOutputFullMedia(unittest.TestCase):
    """ServiceDeviceOutputFullMedia unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDeviceOutputFullMedia:
        """Test ServiceDeviceOutputFullMedia
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDeviceOutputFullMedia`
        """
        model = ServiceDeviceOutputFullMedia()
        if include_optional:
            return ServiceDeviceOutputFullMedia(
                audio = openapi_client.models.service/device_output_full_media_audio.service.DeviceOutputFullMediaAudio(
                    codecs = [
                        ''
                        ], )
            )
        else:
            return ServiceDeviceOutputFullMedia(
        )
        """

    def testServiceDeviceOutputFullMedia(self):
        """Test ServiceDeviceOutputFullMedia"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
