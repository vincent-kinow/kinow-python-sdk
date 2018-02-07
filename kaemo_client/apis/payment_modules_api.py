# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.203
    
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


class PaymentModulesApi(object):
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

    def get_payment_modules(self, **kwargs):
        """
        Get payment modules list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_modules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PaymentModules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_modules_with_http_info(**kwargs)
        else:
            (data) = self.get_payment_modules_with_http_info(**kwargs)
            return data

    def get_payment_modules_with_http_info(self, **kwargs):
        """
        Get payment modules list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_modules_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PaymentModules
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
                    " to method get_payment_modules" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/payment-modules'.replace('{format}', 'json')
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
                                        response_type='PaymentModules',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_payment_url(self, cart_id, payment_name, **kwargs):
        """
        Get payment url
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_url(cart_id, payment_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str payment_name: Payment module name (required)
        :return: PaymentUrl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_url_with_http_info(cart_id, payment_name, **kwargs)
        else:
            (data) = self.get_payment_url_with_http_info(cart_id, payment_name, **kwargs)
            return data

    def get_payment_url_with_http_info(self, cart_id, payment_name, **kwargs):
        """
        Get payment url
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_url_with_http_info(cart_id, payment_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str payment_name: Payment module name (required)
        :return: PaymentUrl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id', 'payment_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `get_payment_url`")
        # verify the required parameter 'payment_name' is set
        if ('payment_name' not in params) or (params['payment_name'] is None):
            raise ValueError("Missing the required parameter `payment_name` when calling `get_payment_url`")


        collection_formats = {}

        resource_path = '/carts/{cart_id}/payments/{payment_name}'.replace('{format}', 'json')
        path_params = {}
        if 'cart_id' in params:
            path_params['cart_id'] = params['cart_id']
        if 'payment_name' in params:
            path_params['payment_name'] = params['payment_name']

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
                                        response_type='PaymentUrl',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def validate_cart(self, cart_id, payment_name, payment_arguments, **kwargs):
        """
        Validate order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_cart(cart_id, payment_name, payment_arguments, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str payment_name: Payment module name (required)
        :param PaymentArguments payment_arguments: payment arguments, token and tokenType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_cart_with_http_info(cart_id, payment_name, payment_arguments, **kwargs)
        else:
            (data) = self.validate_cart_with_http_info(cart_id, payment_name, payment_arguments, **kwargs)
            return data

    def validate_cart_with_http_info(self, cart_id, payment_name, payment_arguments, **kwargs):
        """
        Validate order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_cart_with_http_info(cart_id, payment_name, payment_arguments, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str payment_name: Payment module name (required)
        :param PaymentArguments payment_arguments: payment arguments, token and tokenType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id', 'payment_name', 'payment_arguments']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_cart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `validate_cart`")
        # verify the required parameter 'payment_name' is set
        if ('payment_name' not in params) or (params['payment_name'] is None):
            raise ValueError("Missing the required parameter `payment_name` when calling `validate_cart`")
        # verify the required parameter 'payment_arguments' is set
        if ('payment_arguments' not in params) or (params['payment_arguments'] is None):
            raise ValueError("Missing the required parameter `payment_arguments` when calling `validate_cart`")


        collection_formats = {}

        resource_path = '/carts/{cart_id}/payments/{payment_name}/validate'.replace('{format}', 'json')
        path_params = {}
        if 'cart_id' in params:
            path_params['cart_id'] = params['cart_id']
        if 'payment_name' in params:
            path_params['payment_name'] = params['payment_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_arguments' in params:
            body_params = params['payment_arguments']

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
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def validate_free_order(self, cart_id, **kwargs):
        """
        Validate cart without payment method (only for carts with a total of 0)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_free_order(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to validate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_free_order_with_http_info(cart_id, **kwargs)
        else:
            (data) = self.validate_free_order_with_http_info(cart_id, **kwargs)
            return data

    def validate_free_order_with_http_info(self, cart_id, **kwargs):
        """
        Validate cart without payment method (only for carts with a total of 0)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_free_order_with_http_info(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to validate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_free_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `validate_free_order`")


        collection_formats = {}

        resource_path = '/carts/{cart_id}/validate-free-order'.replace('{format}', 'json')
        path_params = {}
        if 'cart_id' in params:
            path_params['cart_id'] = params['cart_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
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
