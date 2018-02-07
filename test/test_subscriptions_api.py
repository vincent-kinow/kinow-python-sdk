# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.200
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.subscriptions_api import SubscriptionsApi


class TestSubscriptionsApi(unittest.TestCase):
    """ SubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.subscriptions_api.SubscriptionsApi()

    def tearDown(self):
        pass

    def test_get_disabled_subscriptions(self):
        """
        Test case for get_disabled_subscriptions

        
        """
        pass

    def test_get_subscription(self):
        """
        Test case for get_subscription

        
        """
        pass

    def test_get_subscription_categories(self):
        """
        Test case for get_subscription_categories

        
        """
        pass

    def test_get_subscription_cover_image(self):
        """
        Test case for get_subscription_cover_image

        
        """
        pass

    def test_get_subscriptions(self):
        """
        Test case for get_subscriptions

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
