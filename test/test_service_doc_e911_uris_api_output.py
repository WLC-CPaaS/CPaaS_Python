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

from openapi_client.models.service_doc_e911_uris_api_output import ServiceDocE911URIsApiOutput

class TestServiceDocE911URIsApiOutput(unittest.TestCase):
    """ServiceDocE911URIsApiOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocE911URIsApiOutput:
        """Test ServiceDocE911URIsApiOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocE911URIsApiOutput`
        """
        model = ServiceDocE911URIsApiOutput()
        if include_optional:
            return ServiceDocE911URIsApiOutput(
                data = [
                    openapi_client.models.repository/locations_response.repository.LocationsResponse(
                        location_id = '', 
                        phone_number = '', )
                    ],
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocE911URIsApiOutput(
        )
        """

    def testServiceDocE911URIsApiOutput(self):
        """Test ServiceDocE911URIsApiOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
