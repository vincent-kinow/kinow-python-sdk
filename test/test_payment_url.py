# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: blabla
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.payment_url import PaymentUrl


class TestPaymentUrl(unittest.TestCase):
    """ PaymentUrl unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentUrl(self):
        """
        Test PaymentUrl
        """
        model = kaemo_client.models.payment_url.PaymentUrl()


if __name__ == '__main__':
    unittest.main()
