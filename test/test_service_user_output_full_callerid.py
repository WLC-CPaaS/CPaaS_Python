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

from openapi_client.models.service_user_output_full_callerid import ServiceUserOutputFullCallerid

class TestServiceUserOutputFullCallerid(unittest.TestCase):
    """ServiceUserOutputFullCallerid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUserOutputFullCallerid:
        """Test ServiceUserOutputFullCallerid
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUserOutputFullCallerid`
        """
        model = ServiceUserOutputFullCallerid()
        if include_optional:
            return ServiceUserOutputFullCallerid(
                emergency = openapi_client.models.service/user_output_full_callerid_emergency.service.UserOutputFullCalleridEmergency(
                    number = '', ),
                external = openapi_client.models.service/user_output_full_callerid_external.service.UserOutputFullCalleridExternal(
                    number = '', ),
                internal = openapi_client.models.service/user_output_full_callerid_internal.service.UserOutputFullCalleridInternal(
                    number = '', )
            )
        else:
            return ServiceUserOutputFullCallerid(
        )
        """

    def testServiceUserOutputFullCallerid(self):
        """Test ServiceUserOutputFullCallerid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
