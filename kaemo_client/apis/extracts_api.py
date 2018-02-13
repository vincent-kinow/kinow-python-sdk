# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.365
    
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


class ExtractsApi(object):
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

    def create_extract(self, body, **kwargs):
        """
        Create new extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_extract(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Extract body:  (required)
        :return: Extract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_extract_with_http_info(body, **kwargs)
        else:
            (data) = self.create_extract_with_http_info(body, **kwargs)
            return data

    def create_extract_with_http_info(self, body, **kwargs):
        """
        Create new extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_extract_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Extract body:  (required)
        :return: Extract
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_extract" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_extract`")


        collection_formats = {}

        resource_path = '/extracts'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='Extract',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_extract(self, extract_id, **kwargs):
        """
        Delete extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_extract(extract_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the video to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_extract_with_http_info(extract_id, **kwargs)
        else:
            (data) = self.delete_extract_with_http_info(extract_id, **kwargs)
            return data

    def delete_extract_with_http_info(self, extract_id, **kwargs):
        """
        Delete extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_extract_with_http_info(extract_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the video to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extract_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_extract" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extract_id' is set
        if ('extract_id' not in params) or (params['extract_id'] is None):
            raise ValueError("Missing the required parameter `extract_id` when calling `delete_extract`")


        collection_formats = {}

        resource_path = '/extracts/{extract_id}'.replace('{format}', 'json')
        path_params = {}
        if 'extract_id' in params:
            path_params['extract_id'] = params['extract_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_extract_player(self, extract_id, **kwargs):
        """
        Get extract's player
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_extract_player(extract_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the extract to fetch (required)
        :return: PlayerConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_extract_player_with_http_info(extract_id, **kwargs)
        else:
            (data) = self.get_extract_player_with_http_info(extract_id, **kwargs)
            return data

    def get_extract_player_with_http_info(self, extract_id, **kwargs):
        """
        Get extract's player
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_extract_player_with_http_info(extract_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the extract to fetch (required)
        :return: PlayerConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extract_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extract_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extract_id' is set
        if ('extract_id' not in params) or (params['extract_id'] is None):
            raise ValueError("Missing the required parameter `extract_id` when calling `get_extract_player`")


        collection_formats = {}

        resource_path = '/extracts/{extract_id}/player'.replace('{format}', 'json')
        path_params = {}
        if 'extract_id' in params:
            path_params['extract_id'] = params['extract_id']

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
                                        response_type='PlayerConfiguration',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_extracts(self, product_id, **kwargs):
        """
        Get extracts of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_extracts(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :param int page:
        :param int per_page:
        :return: ProductExtractsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_extracts_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_extracts_with_http_info(product_id, **kwargs)
            return data

    def get_product_extracts_with_http_info(self, product_id, **kwargs):
        """
        Get extracts of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_extracts_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :param int page:
        :param int per_page:
        :return: ProductExtractsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_extracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_extracts`")


        collection_formats = {}

        resource_path = '/products/{product_id}/extracts'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

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
                                        response_type='ProductExtractsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_extract(self, extract_id, body, **kwargs):
        """
        Update extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_extract(extract_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the video to update (required)
        :param Extract body:  (required)
        :return: Extract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_extract_with_http_info(extract_id, body, **kwargs)
        else:
            (data) = self.update_extract_with_http_info(extract_id, body, **kwargs)
            return data

    def update_extract_with_http_info(self, extract_id, body, **kwargs):
        """
        Update extract
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_extract_with_http_info(extract_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int extract_id: ID of the video to update (required)
        :param Extract body:  (required)
        :return: Extract
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extract_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_extract" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extract_id' is set
        if ('extract_id' not in params) or (params['extract_id'] is None):
            raise ValueError("Missing the required parameter `extract_id` when calling `update_extract`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_extract`")


        collection_formats = {}

        resource_path = '/extracts/{extract_id}'.replace('{format}', 'json')
        path_params = {}
        if 'extract_id' in params:
            path_params['extract_id'] = params['extract_id']

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

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Extract',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
