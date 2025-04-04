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

from openapi_client.api.group_api import GroupApi


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GroupApi()

    def tearDown(self) -> None:
        pass

    def test_v1_account_account_id_group_get(self) -> None:
        """Test case for v1_account_account_id_group_get

        Get Group List
        """
        pass

    def test_v1_account_account_id_group_group_id_delete(self) -> None:
        """Test case for v1_account_account_id_group_group_id_delete

        Delete Group
        """
        pass

    def test_v1_account_account_id_group_group_id_get(self) -> None:
        """Test case for v1_account_account_id_group_group_id_get

        Get Group Details
        """
        pass

    def test_v1_account_account_id_group_group_id_put(self) -> None:
        """Test case for v1_account_account_id_group_group_id_put

        Update Group
        """
        pass

    def test_v1_account_account_id_group_post(self) -> None:
        """Test case for v1_account_account_id_group_post

        Create Group
        """
        pass


if __name__ == '__main__':
    unittest.main()
