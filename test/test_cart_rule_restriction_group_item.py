# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.361
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.cart_rule_restriction_group_item import CartRuleRestrictionGroupItem


class TestCartRuleRestrictionGroupItem(unittest.TestCase):
    """ CartRuleRestrictionGroupItem unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartRuleRestrictionGroupItem(self):
        """
        Test CartRuleRestrictionGroupItem
        """
        model = kaemo_client.models.cart_rule_restriction_group_item.CartRuleRestrictionGroupItem()


if __name__ == '__main__':
    unittest.main()
