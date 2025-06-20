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

from openapi_client.models.models_template import ModelsTemplate

class TestModelsTemplate(unittest.TestCase):
    """ModelsTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelsTemplate:
        """Test ModelsTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelsTemplate`
        """
        model = ModelsTemplate()
        if include_optional:
            return ModelsTemplate(
                brand_name = '',
                created_at = '',
                family_name = '',
                firmware_id = '',
                firmware_version = '',
                id = '',
                is_active = True,
                model_name = '',
                template_name = '',
                updated_at = ''
            )
        else:
            return ModelsTemplate(
        )
        """

    def testModelsTemplate(self):
        """Test ModelsTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
