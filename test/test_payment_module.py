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
from kaemo_client.models.payment_module import PaymentModule


class TestPaymentModule(unittest.TestCase):
    """ PaymentModule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentModule(self):
        """
        Test PaymentModule
        """
        model = kaemo_client.models.payment_module.PaymentModule()


if __name__ == '__main__':
    unittest.main()
