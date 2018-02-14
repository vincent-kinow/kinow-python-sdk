# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 0.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.cms_categories_lists import CMSCategoriesLists


class TestCMSCategoriesLists(unittest.TestCase):
    """ CMSCategoriesLists unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCMSCategoriesLists(self):
        """
        Test CMSCategoriesLists
        """
        model = kaemo_client.models.cms_categories_lists.CMSCategoriesLists()


if __name__ == '__main__':
    unittest.main()
