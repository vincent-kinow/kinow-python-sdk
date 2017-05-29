# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, description=None, priority=None, partial_use=None, code=None, active=None, date_add=None, date_upd=None, name=None):
        """
        CartRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'description': 'str',
            'priority': 'int',
            'partial_use': 'bool',
            'code': 'str',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'name': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'description': 'description',
            'priority': 'priority',
            'partial_use': 'partial_use',
            'code': 'code',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'name': 'name'
        }

        self._id = id
        self._id_customer = id_customer
        self._description = description
        self._priority = priority
        self._partial_use = partial_use
        self._code = code
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this CartRule.

        :return: The id of this CartRule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CartRule.

        :param id: The id of this CartRule.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CartRule.

        :return: The id_customer of this CartRule.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CartRule.

        :param id_customer: The id_customer of this CartRule.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def description(self):
        """
        Gets the description of this CartRule.

        :return: The description of this CartRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CartRule.

        :param description: The description of this CartRule.
        :type: str
        """

        self._description = description

    @property
    def priority(self):
        """
        Gets the priority of this CartRule.

        :return: The priority of this CartRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CartRule.

        :param priority: The priority of this CartRule.
        :type: int
        """

        self._priority = priority

    @property
    def partial_use(self):
        """
        Gets the partial_use of this CartRule.

        :return: The partial_use of this CartRule.
        :rtype: bool
        """
        return self._partial_use

    @partial_use.setter
    def partial_use(self, partial_use):
        """
        Sets the partial_use of this CartRule.

        :param partial_use: The partial_use of this CartRule.
        :type: bool
        """

        self._partial_use = partial_use

    @property
    def code(self):
        """
        Gets the code of this CartRule.

        :return: The code of this CartRule.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CartRule.

        :param code: The code of this CartRule.
        :type: str
        """

        self._code = code

    @property
    def active(self):
        """
        Gets the active of this CartRule.

        :return: The active of this CartRule.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CartRule.

        :param active: The active of this CartRule.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this CartRule.

        :return: The date_add of this CartRule.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this CartRule.

        :param date_add: The date_add of this CartRule.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this CartRule.

        :return: The date_upd of this CartRule.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this CartRule.

        :param date_upd: The date_upd of this CartRule.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def name(self):
        """
        Gets the name of this CartRule.

        :return: The name of this CartRule.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CartRule.

        :param name: The name of this CartRule.
        :type: list[I18nField]
        """

        self._name = name

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
