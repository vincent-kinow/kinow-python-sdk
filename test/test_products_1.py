# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.365
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.products_1 import Products1


class TestProducts1(unittest.TestCase):
    """ Products1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProducts1(self):
        """
        Test Products1
        """
        model = kaemo_client.models.products_1.Products1()


if __name__ == '__main__':
    unittest.main()
