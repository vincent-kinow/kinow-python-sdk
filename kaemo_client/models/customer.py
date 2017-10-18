# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, lastname=None, firstname=None, email=None, id_gender=None, birthday=None, newsletter=None, optin=None, active=None, id_lang=None, date_add=None, date_upd=None, password=None, id_country=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'lastname': 'str',
            'firstname': 'str',
            'email': 'str',
            'id_gender': 'int',
            'birthday': 'str',
            'newsletter': 'bool',
            'optin': 'bool',
            'active': 'bool',
            'id_lang': 'int',
            'date_add': 'str',
            'date_upd': 'str',
            'password': 'str',
            'id_country': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'lastname': 'lastname',
            'firstname': 'firstname',
            'email': 'email',
            'id_gender': 'id_gender',
            'birthday': 'birthday',
            'newsletter': 'newsletter',
            'optin': 'optin',
            'active': 'active',
            'id_lang': 'id_lang',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'password': 'password',
            'id_country': 'id_country'
        }

        self._id = id
        self._lastname = lastname
        self._firstname = firstname
        self._email = email
        self._id_gender = id_gender
        self._birthday = birthday
        self._newsletter = newsletter
        self._optin = optin
        self._active = active
        self._id_lang = id_lang
        self._date_add = date_add
        self._date_upd = date_upd
        self._password = password
        self._id_country = id_country

    @property
    def id(self):
        """
        Gets the id of this Customer.

        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.

        :param id: The id of this Customer.
        :type: int
        """

        self._id = id

    @property
    def lastname(self):
        """
        Gets the lastname of this Customer.

        :return: The lastname of this Customer.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Customer.

        :param lastname: The lastname of this Customer.
        :type: str
        """

        self._lastname = lastname

    @property
    def firstname(self):
        """
        Gets the firstname of this Customer.

        :return: The firstname of this Customer.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Customer.

        :param firstname: The firstname of this Customer.
        :type: str
        """

        self._firstname = firstname

    @property
    def email(self):
        """
        Gets the email of this Customer.

        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Customer.

        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def id_gender(self):
        """
        Gets the id_gender of this Customer.

        :return: The id_gender of this Customer.
        :rtype: int
        """
        return self._id_gender

    @id_gender.setter
    def id_gender(self, id_gender):
        """
        Sets the id_gender of this Customer.

        :param id_gender: The id_gender of this Customer.
        :type: int
        """

        self._id_gender = id_gender

    @property
    def birthday(self):
        """
        Gets the birthday of this Customer.

        :return: The birthday of this Customer.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this Customer.

        :param birthday: The birthday of this Customer.
        :type: str
        """

        self._birthday = birthday

    @property
    def newsletter(self):
        """
        Gets the newsletter of this Customer.

        :return: The newsletter of this Customer.
        :rtype: bool
        """
        return self._newsletter

    @newsletter.setter
    def newsletter(self, newsletter):
        """
        Sets the newsletter of this Customer.

        :param newsletter: The newsletter of this Customer.
        :type: bool
        """

        self._newsletter = newsletter

    @property
    def optin(self):
        """
        Gets the optin of this Customer.

        :return: The optin of this Customer.
        :rtype: bool
        """
        return self._optin

    @optin.setter
    def optin(self, optin):
        """
        Sets the optin of this Customer.

        :param optin: The optin of this Customer.
        :type: bool
        """

        self._optin = optin

    @property
    def active(self):
        """
        Gets the active of this Customer.

        :return: The active of this Customer.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Customer.

        :param active: The active of this Customer.
        :type: bool
        """

        self._active = active

    @property
    def id_lang(self):
        """
        Gets the id_lang of this Customer.

        :return: The id_lang of this Customer.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this Customer.

        :param id_lang: The id_lang of this Customer.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def date_add(self):
        """
        Gets the date_add of this Customer.

        :return: The date_add of this Customer.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Customer.

        :param date_add: The date_add of this Customer.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Customer.

        :return: The date_upd of this Customer.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Customer.

        :param date_upd: The date_upd of this Customer.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def password(self):
        """
        Gets the password of this Customer.
        Only available in body

        :return: The password of this Customer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Customer.
        Only available in body

        :param password: The password of this Customer.
        :type: str
        """

        self._password = password

    @property
    def id_country(self):
        """
        Gets the id_country of this Customer.
        Only available in body

        :return: The id_country of this Customer.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this Customer.
        Only available in body

        :param id_country: The id_country of this Customer.
        :type: int
        """

        self._id_country = id_country

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
