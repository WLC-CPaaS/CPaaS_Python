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

from openapi_client.api.account_api import AccountApi


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountApi()

    def tearDown(self) -> None:
        pass

    def test_v1_account_accountid_children_get(self) -> None:
        """Test case for v1_account_accountid_children_get

        Get Sub Account List
        """
        pass

    def test_v1_account_accountid_delete(self) -> None:
        """Test case for v1_account_accountid_delete

        Delete Account
        """
        pass

    def test_v1_account_accountid_dnsrecord_get(self) -> None:
        """Test case for v1_account_accountid_dnsrecord_get

        Get Account DNS Record
        """
        pass

    def test_v1_account_accountid_dnsrecord_post(self) -> None:
        """Test case for v1_account_accountid_dnsrecord_post

        Create Account DNS Record
        """
        pass

    def test_v1_account_accountid_dnsrecord_put(self) -> None:
        """Test case for v1_account_accountid_dnsrecord_put

        Convert Account DNS Record
        """
        pass

    def test_v1_account_accountid_get(self) -> None:
        """Test case for v1_account_accountid_get

        Get Account Details
        """
        pass

    def test_v1_account_accountid_limit_get(self) -> None:
        """Test case for v1_account_accountid_limit_get

        Get Account Limits
        """
        pass

    def test_v1_account_accountid_limit_put(self) -> None:
        """Test case for v1_account_accountid_limit_put

        Set Account Limits
        """
        pass

    def test_v1_account_accountid_post(self) -> None:
        """Test case for v1_account_accountid_post

        Create Sub Account
        """
        pass

    def test_v1_account_accountid_put(self) -> None:
        """Test case for v1_account_accountid_put

        Update Account
        """
        pass

    def test_v1_account_apikey_get(self) -> None:
        """Test case for v1_account_apikey_get

        """
        pass

    def test_v1_account_get(self) -> None:
        """Test case for v1_account_get

        Get Account List
        """
        pass

    def test_v1_account_post(self) -> None:
        """Test case for v1_account_post

        Create Account
        """
        pass


if __name__ == '__main__':
    unittest.main()
