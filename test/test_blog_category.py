# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 0.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.blog_category import BlogCategory


class TestBlogCategory(unittest.TestCase):
    """ BlogCategory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlogCategory(self):
        """
        Test BlogCategory
        """
        model = kaemo_client.models.blog_category.BlogCategory()


if __name__ == '__main__':
    unittest.main()
