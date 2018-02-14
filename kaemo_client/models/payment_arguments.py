# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 0.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentArguments(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, token=None, token_type=None):
        """
        PaymentArguments - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'token': 'str',
            'token_type': 'str'
        }

        self.attribute_map = {
            'token': 'token',
            'token_type': 'tokenType'
        }

        self._token = token
        self._token_type = token_type

    @property
    def token(self):
        """
        Gets the token of this PaymentArguments.

        :return: The token of this PaymentArguments.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this PaymentArguments.

        :param token: The token of this PaymentArguments.
        :type: str
        """

        self._token = token

    @property
    def token_type(self):
        """
        Gets the token_type of this PaymentArguments.

        :return: The token_type of this PaymentArguments.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this PaymentArguments.

        :param token_type: The token_type of this PaymentArguments.
        :type: str
        """

        self._token_type = token_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
