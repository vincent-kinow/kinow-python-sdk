# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.151
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoViews(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, played=None, views=None):
        """
        VideoViews - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'played': 'int',
            'views': 'str'
        }

        self.attribute_map = {
            'played': 'played',
            'views': 'views'
        }

        self._played = played
        self._views = views

    @property
    def played(self):
        """
        Gets the played of this VideoViews.
        Number of times the video was played

        :return: The played of this VideoViews.
        :rtype: int
        """
        return self._played

    @played.setter
    def played(self, played):
        """
        Sets the played of this VideoViews.
        Number of times the video was played

        :param played: The played of this VideoViews.
        :type: int
        """

        self._played = played

    @property
    def views(self):
        """
        Gets the views of this VideoViews.
        Total number of views

        :return: The views of this VideoViews.
        :rtype: str
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this VideoViews.
        Total number of views

        :param views: The views of this VideoViews.
        :type: str
        """

        self._views = views

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
