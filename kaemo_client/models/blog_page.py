# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BlogPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_lang=None, title=None, link_rewrite=None, description_short=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, date_add=None, date_issue=None, date_upd=None, active=None):
        """
        BlogPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_lang': 'int',
            'title': 'str',
            'link_rewrite': 'str',
            'description_short': 'str',
            'description': 'str',
            'meta_title': 'int',
            'meta_description': 'str',
            'meta_keywords': 'str',
            'date_add': 'str',
            'date_issue': 'str',
            'date_upd': 'str',
            'active': 'int'
        }

        self.attribute_map = {
            'id_lang': 'id_lang',
            'title': 'title',
            'link_rewrite': 'link_rewrite',
            'description_short': 'description_short',
            'description': 'description',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'date_add': 'date_add',
            'date_issue': 'date_issue',
            'date_upd': 'date_upd',
            'active': 'active'
        }

        self._id_lang = id_lang
        self._title = title
        self._link_rewrite = link_rewrite
        self._description_short = description_short
        self._description = description
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._date_add = date_add
        self._date_issue = date_issue
        self._date_upd = date_upd
        self._active = active

    @property
    def id_lang(self):
        """
        Gets the id_lang of this BlogPage.

        :return: The id_lang of this BlogPage.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this BlogPage.

        :param id_lang: The id_lang of this BlogPage.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def title(self):
        """
        Gets the title of this BlogPage.

        :return: The title of this BlogPage.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this BlogPage.

        :param title: The title of this BlogPage.
        :type: str
        """

        self._title = title

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this BlogPage.

        :return: The link_rewrite of this BlogPage.
        :rtype: str
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this BlogPage.

        :param link_rewrite: The link_rewrite of this BlogPage.
        :type: str
        """

        self._link_rewrite = link_rewrite

    @property
    def description_short(self):
        """
        Gets the description_short of this BlogPage.

        :return: The description_short of this BlogPage.
        :rtype: str
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this BlogPage.

        :param description_short: The description_short of this BlogPage.
        :type: str
        """

        self._description_short = description_short

    @property
    def description(self):
        """
        Gets the description of this BlogPage.

        :return: The description of this BlogPage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlogPage.

        :param description: The description of this BlogPage.
        :type: str
        """

        self._description = description

    @property
    def meta_title(self):
        """
        Gets the meta_title of this BlogPage.

        :return: The meta_title of this BlogPage.
        :rtype: int
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this BlogPage.

        :param meta_title: The meta_title of this BlogPage.
        :type: int
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this BlogPage.

        :return: The meta_description of this BlogPage.
        :rtype: str
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this BlogPage.

        :param meta_description: The meta_description of this BlogPage.
        :type: str
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this BlogPage.

        :return: The meta_keywords of this BlogPage.
        :rtype: str
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this BlogPage.

        :param meta_keywords: The meta_keywords of this BlogPage.
        :type: str
        """

        self._meta_keywords = meta_keywords

    @property
    def date_add(self):
        """
        Gets the date_add of this BlogPage.

        :return: The date_add of this BlogPage.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this BlogPage.

        :param date_add: The date_add of this BlogPage.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_issue(self):
        """
        Gets the date_issue of this BlogPage.

        :return: The date_issue of this BlogPage.
        :rtype: str
        """
        return self._date_issue

    @date_issue.setter
    def date_issue(self, date_issue):
        """
        Sets the date_issue of this BlogPage.

        :param date_issue: The date_issue of this BlogPage.
        :type: str
        """

        self._date_issue = date_issue

    @property
    def date_upd(self):
        """
        Gets the date_upd of this BlogPage.

        :return: The date_upd of this BlogPage.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this BlogPage.

        :param date_upd: The date_upd of this BlogPage.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def active(self):
        """
        Gets the active of this BlogPage.

        :return: The active of this BlogPage.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this BlogPage.

        :param active: The active of this BlogPage.
        :type: int
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
