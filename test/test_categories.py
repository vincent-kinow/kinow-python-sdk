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
from kaemo_client.models.categories import Categories


class TestCategories(unittest.TestCase):
    """ Categories unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategories(self):
        """
        Test Categories
        """
        model = kaemo_client.models.categories.Categories()


if __name__ == '__main__':
    unittest.main()
