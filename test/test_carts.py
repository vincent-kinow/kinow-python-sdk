# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.70
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.carts import Carts


class TestCarts(unittest.TestCase):
    """ Carts unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCarts(self):
        """
        Test Carts
        """
        model = kaemo_client.models.carts.Carts()


if __name__ == '__main__':
    unittest.main()
