# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.33
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.o_auth_api import OAuthApi


class TestOAuthApi(unittest.TestCase):
    """ OAuthApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.o_auth_api.OAuthApi()

    def tearDown(self):
        pass

    def test_get_token(self):
        """
        Test case for get_token

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
