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
from kaemo_client.apis.currencies_api import CurrenciesApi


class TestCurrenciesApi(unittest.TestCase):
    """ CurrenciesApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.currencies_api.CurrenciesApi()

    def tearDown(self):
        pass

    def test_get_currencies(self):
        """
        Test case for get_currencies

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
