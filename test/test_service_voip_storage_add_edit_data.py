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

from openapi_client.models.service_voip_storage_add_edit_data import ServiceVOIPStorageAddEditData

class TestServiceVOIPStorageAddEditData(unittest.TestCase):
    """ServiceVOIPStorageAddEditData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceVOIPStorageAddEditData:
        """Test ServiceVOIPStorageAddEditData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceVOIPStorageAddEditData`
        """
        model = ServiceVOIPStorageAddEditData()
        if include_optional:
            return ServiceVOIPStorageAddEditData(
                attachments = { },
                connections = { },
                id = '',
                plan = openapi_client.models.service/storage_plan.service.StoragePlan(
                    account = openapi_client.models.service/storage_plan_database.service.StoragePlanDatabase(
                        attachments = openapi_client.models.service/storage_plan_database_attachment.service.StoragePlanDatabaseAttachment(
                            handler = '', 
                            params = { }, 
                            stub = True, ), 
                        connection = '', 
                        database = openapi_client.models.service/storage_plan_database_properties.service.StoragePlanDatabaseProperties(
                            create_options = { }, 
                            names = [
                                ''
                                ], ), 
                        types = openapi_client.models.service/storage_plan_database_types.service.StoragePlanDatabaseTypes(
                            call_recording = openapi_client.models.service/storage_plan_database_document.service.StoragePlanDatabaseDocument(
                                connection = '', ), 
                            fax = openapi_client.models.service/storage_plan_database_document.service.StoragePlanDatabaseDocument(
                                connection = '', ), 
                            function = , 
                            mailbox_message = , 
                            media = , ), ), 
                    aggregate = openapi_client.models.service/storage_plan_database.service.StoragePlanDatabase(
                        connection = '', ), 
                    modb = , 
                    system = , )
            )
        else:
            return ServiceVOIPStorageAddEditData(
        )
        """

    def testServiceVOIPStorageAddEditData(self):
        """Test ServiceVOIPStorageAddEditData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
