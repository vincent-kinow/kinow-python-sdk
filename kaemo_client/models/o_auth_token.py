# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 0.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OAuthToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, token_type=None, expires_in=None, access_token=None, refresh_token=None):
        """
        OAuthToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'token_type': 'str',
            'expires_in': 'int',
            'access_token': 'str',
            'refresh_token': 'str'
        }

        self.attribute_map = {
            'token_type': 'token_type',
            'expires_in': 'expires_in',
            'access_token': 'access_token',
            'refresh_token': 'refresh_token'
        }

        self._token_type = token_type
        self._expires_in = expires_in
        self._access_token = access_token
        self._refresh_token = refresh_token

    @property
    def token_type(self):
        """
        Gets the token_type of this OAuthToken.

        :return: The token_type of this OAuthToken.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this OAuthToken.

        :param token_type: The token_type of this OAuthToken.
        :type: str
        """

        self._token_type = token_type

    @property
    def expires_in(self):
        """
        Gets the expires_in of this OAuthToken.

        :return: The expires_in of this OAuthToken.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this OAuthToken.

        :param expires_in: The expires_in of this OAuthToken.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def access_token(self):
        """
        Gets the access_token of this OAuthToken.

        :return: The access_token of this OAuthToken.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this OAuthToken.

        :param access_token: The access_token of this OAuthToken.
        :type: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this OAuthToken.

        :return: The refresh_token of this OAuthToken.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this OAuthToken.

        :param refresh_token: The refresh_token of this OAuthToken.
        :type: str
        """

        self._refresh_token = refresh_token

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
