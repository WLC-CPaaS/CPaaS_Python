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

from openapi_client.models.service_doc_e911_locations_uri_api_output import ServiceDocE911LocationsURIApiOutput

class TestServiceDocE911LocationsURIApiOutput(unittest.TestCase):
    """ServiceDocE911LocationsURIApiOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocE911LocationsURIApiOutput:
        """Test ServiceDocE911LocationsURIApiOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocE911LocationsURIApiOutput`
        """
        model = ServiceDocE911LocationsURIApiOutput()
        if include_optional:
            return ServiceDocE911LocationsURIApiOutput(
                data = [
                    openapi_client.models.service/e911_location_uri.service.E911LocationURI(
                        activated_time = '', 
                        address1 = '', 
                        address2 = '', 
                        caller_name = '', 
                        comments = '', 
                        community = '', 
                        customer_order_id = '', 
                        latitude = 1.337, 
                        legacy_data = openapi_client.models.service_e911_location_uri_legacy_data.service_E911LocationURI_legacyData(
                            house_number = '', 
                            predirectional = '', 
                            street_name = '', 
                            suite = '', ), 
                        location_id = '', 
                        longitude = 1.337, 
                        plus_four = '', 
                        postal_code = '', 
                        state = '', 
                        status = openapi_client.models.service_e911_location_uri_status.service_E911LocationURI_status(
                            code = '', 
                            description = '', ), 
                        type = '', 
                        update_time = '', )
                    ],
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocE911LocationsURIApiOutput(
        )
        """

    def testServiceDocE911LocationsURIApiOutput(self):
        """Test ServiceDocE911LocationsURIApiOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
