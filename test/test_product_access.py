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
from kaemo_client.models.product_access import ProductAccess


class TestProductAccess(unittest.TestCase):
    """ ProductAccess unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAccess(self):
        """
        Test ProductAccess
        """
        model = kaemo_client.models.product_access.ProductAccess()


if __name__ == '__main__':
    unittest.main()
