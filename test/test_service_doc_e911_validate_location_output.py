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

from openapi_client.models.service_doc_e911_validate_location_output import ServiceDocE911ValidateLocationOutput

class TestServiceDocE911ValidateLocationOutput(unittest.TestCase):
    """ServiceDocE911ValidateLocationOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDocE911ValidateLocationOutput:
        """Test ServiceDocE911ValidateLocationOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDocE911ValidateLocationOutput`
        """
        model = ServiceDocE911ValidateLocationOutput()
        if include_optional:
            return ServiceDocE911ValidateLocationOutput(
                data = openapi_client.models.service/e911_validate_location_output.service.E911ValidateLocationOutput(
                    location = openapi_client.models.service/e911_location_output.service.E911LocationOutput(
                        activated_time = '', 
                        address_1 = '', 
                        address_2 = '', 
                        caller_name = '', 
                        comments = '', 
                        community = '', 
                        customer_order_id = '', 
                        latitude = 1.337, 
                        legacy_data = openapi_client.models.service/e911_legacy_data_output.service.E911LegacyDataOutput(
                            house_number = '', 
                            predirectional = '', 
                            street_name = '', 
                            suite = '', ), 
                        location_id = '', 
                        longitude = 1.337, 
                        plus_four = '', 
                        postal_code = '', 
                        state = '', 
                        status = openapi_client.models.service/e911_status_output.service.E911StatusOutput(
                            code = '', 
                            description = '', ), 
                        type = '', 
                        update_time = '', ), ),
                request_id = '',
                status_code = 56
            )
        else:
            return ServiceDocE911ValidateLocationOutput(
        )
        """

    def testServiceDocE911ValidateLocationOutput(self):
        """Test ServiceDocE911ValidateLocationOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
