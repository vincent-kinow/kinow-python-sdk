# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.359
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttributeUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, price=None, active=None):
        """
        ProductAttributeUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'price': 'float',
            'active': 'bool'
        }

        self.attribute_map = {
            'price': 'price',
            'active': 'active'
        }

        self._price = price
        self._active = active

    @property
    def price(self):
        """
        Gets the price of this ProductAttributeUpdateRequest.
        Final price of the product

        :return: The price of this ProductAttributeUpdateRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttributeUpdateRequest.
        Final price of the product

        :param price: The price of this ProductAttributeUpdateRequest.
        :type: float
        """

        self._price = price

    @property
    def active(self):
        """
        Gets the active of this ProductAttributeUpdateRequest.
        Status of the attribute

        :return: The active of this ProductAttributeUpdateRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductAttributeUpdateRequest.
        Status of the attribute

        :param active: The active of this ProductAttributeUpdateRequest.
        :type: bool
        """

        self._active = active

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
