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
from kaemo_client.apis.player_api import PlayerApi


class TestPlayerApi(unittest.TestCase):
    """ PlayerApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.player_api.PlayerApi()

    def tearDown(self):
        pass

    def test_get_extract_player(self):
        """
        Test case for get_extract_player

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
