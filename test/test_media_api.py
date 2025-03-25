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

from openapi_client.api.media_api import MediaApi


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MediaApi()

    def tearDown(self) -> None:
        pass

    def test_v1_account_account_id_media_media_id_file_get(self) -> None:
        """Test case for v1_account_account_id_media_media_id_file_get

        Get Media File
        """
        pass

    def test_v1_account_account_id_media_media_id_file_post(self) -> None:
        """Test case for v1_account_account_id_media_media_id_file_post

        Add Media File
        """
        pass

    def test_v1_account_accountid_media_get(self) -> None:
        """Test case for v1_account_accountid_media_get

        Get Media List
        """
        pass

    def test_v1_account_accountid_media_mediaid_delete(self) -> None:
        """Test case for v1_account_accountid_media_mediaid_delete

        Delete Media
        """
        pass

    def test_v1_account_accountid_media_mediaid_get(self) -> None:
        """Test case for v1_account_accountid_media_mediaid_get

        Get Media Details
        """
        pass

    def test_v1_account_accountid_media_post(self) -> None:
        """Test case for v1_account_accountid_media_post

        Create Media
        """
        pass


if __name__ == '__main__':
    unittest.main()
