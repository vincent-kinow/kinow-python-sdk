# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.customer_id import CustomerId


class TestCustomerId(unittest.TestCase):
    """ CustomerId unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerId(self):
        """
        Test CustomerId
        """
        model = kaemo_client.models.customer_id.CustomerId()


if __name__ == '__main__':
    unittest.main()
