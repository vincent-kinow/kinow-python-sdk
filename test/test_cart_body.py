# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: $CI_BUILD_TAG
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.cart_body import CartBody


class TestCartBody(unittest.TestCase):
    """ CartBody unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartBody(self):
        """
        Test CartBody
        """
        model = kaemo_client.models.cart_body.CartBody()


if __name__ == '__main__':
    unittest.main()
