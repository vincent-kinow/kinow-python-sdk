# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.203
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.product_attribute import ProductAttribute


class TestProductAttribute(unittest.TestCase):
    """ ProductAttribute unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttribute(self):
        """
        Test ProductAttribute
        """
        model = kaemo_client.models.product_attribute.ProductAttribute()


if __name__ == '__main__':
    unittest.main()
