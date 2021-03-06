# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.accesses_api import AccessesApi


class TestAccessesApi(unittest.TestCase):
    """ AccessesApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.accesses_api.AccessesApi()

    def tearDown(self):
        pass

    def test_get_available_categories(self):
        """
        Test case for get_available_categories

        
        """
        pass

    def test_get_available_category(self):
        """
        Test case for get_available_category

        
        """
        pass

    def test_get_customer_has_access_to_product(self):
        """
        Test case for get_customer_has_access_to_product

        
        """
        pass

    def test_get_customer_has_access_to_video(self):
        """
        Test case for get_customer_has_access_to_video

        
        """
        pass

    def test_get_product_availability(self):
        """
        Test case for get_product_availability

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
