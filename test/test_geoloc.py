# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: ./depoy.sh
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.geoloc import Geoloc


class TestGeoloc(unittest.TestCase):
    """ Geoloc unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGeoloc(self):
        """
        Test Geoloc
        """
        model = kaemo_client.models.geoloc.Geoloc()


if __name__ == '__main__':
    unittest.main()
