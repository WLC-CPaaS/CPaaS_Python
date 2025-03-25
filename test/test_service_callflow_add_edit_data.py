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

from openapi_client.models.service_callflow_add_edit_data import ServiceCallflowAddEditData

class TestServiceCallflowAddEditData(unittest.TestCase):
    """ServiceCallflowAddEditData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCallflowAddEditData:
        """Test ServiceCallflowAddEditData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCallflowAddEditData`
        """
        model = ServiceCallflowAddEditData()
        if include_optional:
            return ServiceCallflowAddEditData(
                featurecode = openapi_client.models.service/feature_code.service.FeatureCode(
                    name = '', 
                    number = '', ),
                flow = openapi_client.models.service/callflow_add_edit_flow_data.service.CallflowAddEditFlowData(
                    children = {
                        'key' : openapi_client.models.service/callflow_add_edit_flow_data.service.CallflowAddEditFlowData(
                            data = { }, 
                            module = 'device', )
                        }, 
                    data = { }, 
                    module = 'device', ),
                name = '',
                numbers = [
                    ''
                    ],
                patterns = [
                    ''
                    ]
            )
        else:
            return ServiceCallflowAddEditData(
                numbers = [
                    ''
                    ],
                patterns = [
                    ''
                    ],
        )
        """

    def testServiceCallflowAddEditData(self):
        """Test ServiceCallflowAddEditData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
