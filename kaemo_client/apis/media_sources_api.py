# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: tamere
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MediaSourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_media_source(self, source_id, **kwargs):
        """
        Get media source
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_source(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :return: MediaSource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_media_source_with_http_info(source_id, **kwargs)
        else:
            (data) = self.get_media_source_with_http_info(source_id, **kwargs)
            return data

    def get_media_source_with_http_info(self, source_id, **kwargs):
        """
        Get media source
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_source_with_http_info(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :return: MediaSource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_media_source" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_media_source`")


        collection_formats = {}

        resource_path = '/media-sources/{source_id}'.replace('{format}', 'json')
        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaSource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_media_source_files(self, source_id, **kwargs):
        """
        Get media source files
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_source_files(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :param int page:
        :param int per_page:
        :param str filters:      ```     filters[name][value]=string&filters[name][operator]=contains&filters[date_add][value]=string&filters[date_add][operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```Operator can be strict, contains, gt or lt.
        :return: MediaFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_media_source_files_with_http_info(source_id, **kwargs)
        else:
            (data) = self.get_media_source_files_with_http_info(source_id, **kwargs)
            return data

    def get_media_source_files_with_http_info(self, source_id, **kwargs):
        """
        Get media source files
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_source_files_with_http_info(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :param int page:
        :param int per_page:
        :param str filters:      ```     filters[name][value]=string&filters[name][operator]=contains&filters[date_add][value]=string&filters[date_add][operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```Operator can be strict, contains, gt or lt.
        :return: MediaFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id', 'page', 'per_page', 'filters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_media_source_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_media_source_files`")


        collection_formats = {}

        resource_path = '/media-sources/{source_id}/files'.replace('{format}', 'json')
        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'filters' in params:
            query_params['filters'] = params['filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaFiles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_media_sources(self, **kwargs):
        """
        Get media source list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_sources(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: MediaSources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_media_sources_with_http_info(**kwargs)
        else:
            (data) = self.get_media_sources_with_http_info(**kwargs)
            return data

    def get_media_sources_with_http_info(self, **kwargs):
        """
        Get media source list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_media_sources_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: MediaSources
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_media_sources" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/media-sources'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaSources',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_media_source_files(self, source_id, body, **kwargs):
        """
        Post media file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_media_source_files(source_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :param MediaFile body: Create MediaFile object (required)
        :return: MediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_media_source_files_with_http_info(source_id, body, **kwargs)
        else:
            (data) = self.post_media_source_files_with_http_info(source_id, body, **kwargs)
            return data

    def post_media_source_files_with_http_info(self, source_id, body, **kwargs):
        """
        Post media file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_media_source_files_with_http_info(source_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: ID of the media source to fetch (required)
        :param MediaFile body: Create MediaFile object (required)
        :return: MediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_media_source_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `post_media_source_files`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_media_source_files`")


        collection_formats = {}

        resource_path = '/media-sources/{source_id}/files'.replace('{format}', 'json')
        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        self.api_client.set_default_header('Content-Type', 'application/json')
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaFile',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
