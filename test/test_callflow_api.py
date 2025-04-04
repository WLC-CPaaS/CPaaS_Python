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

from openapi_client.api.callflow_api import CallflowApi


class TestCallflowApi(unittest.TestCase):
    """CallflowApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CallflowApi()

    def tearDown(self) -> None:
        pass

    def test_v1_account_account_id_callflow_callflow_id_delete(self) -> None:
        """Test case for v1_account_account_id_callflow_callflow_id_delete

        Delete Call Group
        """
        pass

    def test_v1_account_account_id_callflow_callflow_id_get(self) -> None:
        """Test case for v1_account_account_id_callflow_callflow_id_get

        Get Call Group Details
        """
        pass

    def test_v1_account_account_id_callflow_callflow_id_put(self) -> None:
        """Test case for v1_account_account_id_callflow_callflow_id_put

        Update Call Group
        """
        pass

    def test_v1_account_account_id_callflow_get(self) -> None:
        """Test case for v1_account_account_id_callflow_get

        Get Callflow List
        """
        pass

    def test_v1_account_account_id_callflow_post(self) -> None:
        """Test case for v1_account_account_id_callflow_post

        Create Call Group
        """
        pass


if __name__ == '__main__':
    unittest.main()
