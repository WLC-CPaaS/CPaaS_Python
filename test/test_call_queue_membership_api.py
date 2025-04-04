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

from openapi_client.api.call_queue_membership_api import CallQueueMembershipApi


class TestCallQueueMembershipApi(unittest.TestCase):
    """CallQueueMembershipApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CallQueueMembershipApi()

    def tearDown(self) -> None:
        pass

    def test_v1_account_account_id_queuemembership_post(self) -> None:
        """Test case for v1_account_account_id_queuemembership_post

        Grant Queue Membership to User
        """
        pass

    def test_v1_account_account_id_queuemembership_recipient_id_disable_post(self) -> None:
        """Test case for v1_account_account_id_queuemembership_recipient_id_disable_post

        Disable Queue Membership
        """
        pass

    def test_v1_account_account_id_queuemembership_recipient_id_enable_post(self) -> None:
        """Test case for v1_account_account_id_queuemembership_recipient_id_enable_post

        Enable Queue Membership
        """
        pass


if __name__ == '__main__':
    unittest.main()
