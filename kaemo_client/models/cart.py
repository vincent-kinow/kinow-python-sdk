# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Cart(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_currency=None, id_customer=None, id_lang=None, date_add=None, date_upd=None, total=None, products=None):
        """
        Cart - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_currency': 'int',
            'id_customer': 'int',
            'id_lang': 'int',
            'date_add': 'str',
            'date_upd': 'str',
            'total': 'int',
            'products': 'list[Product]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_currency': 'id_currency',
            'id_customer': 'id_customer',
            'id_lang': 'id_lang',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'total': 'total',
            'products': 'products'
        }

        self._id = id
        self._id_currency = id_currency
        self._id_customer = id_customer
        self._id_lang = id_lang
        self._date_add = date_add
        self._date_upd = date_upd
        self._total = total
        self._products = products

    @property
    def id(self):
        """
        Gets the id of this Cart.

        :return: The id of this Cart.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cart.

        :param id: The id of this Cart.
        :type: int
        """

        self._id = id

    @property
    def id_currency(self):
        """
        Gets the id_currency of this Cart.

        :return: The id_currency of this Cart.
        :rtype: int
        """
        return self._id_currency

    @id_currency.setter
    def id_currency(self, id_currency):
        """
        Sets the id_currency of this Cart.

        :param id_currency: The id_currency of this Cart.
        :type: int
        """

        self._id_currency = id_currency

    @property
    def id_customer(self):
        """
        Gets the id_customer of this Cart.

        :return: The id_customer of this Cart.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this Cart.

        :param id_customer: The id_customer of this Cart.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_lang(self):
        """
        Gets the id_lang of this Cart.

        :return: The id_lang of this Cart.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this Cart.

        :param id_lang: The id_lang of this Cart.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def date_add(self):
        """
        Gets the date_add of this Cart.

        :return: The date_add of this Cart.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Cart.

        :param date_add: The date_add of this Cart.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Cart.

        :return: The date_upd of this Cart.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Cart.

        :param date_upd: The date_upd of this Cart.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def total(self):
        """
        Gets the total of this Cart.

        :return: The total of this Cart.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this Cart.

        :param total: The total of this Cart.
        :type: int
        """

        self._total = total

    @property
    def products(self):
        """
        Gets the products of this Cart.

        :return: The products of this Cart.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this Cart.

        :param products: The products of this Cart.
        :type: list[Product]
        """

        self._products = products

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
