# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.33
    
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


class ImagesApi(object):
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

    def get_category_banner(self, category_id, **kwargs):
        """
        Get banner of a category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_category_banner(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: ID of the category to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_category_banner_with_http_info(category_id, **kwargs)
        else:
            (data) = self.get_category_banner_with_http_info(category_id, **kwargs)
            return data

    def get_category_banner_with_http_info(self, category_id, **kwargs):
        """
        Get banner of a category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_category_banner_with_http_info(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: ID of the category to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_category_banner" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_category_banner`")


        collection_formats = {}

        resource_path = '/categories/{category_id}/banner'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_intro_image(self, **kwargs):
        """
        Get introduction image
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_intro_image(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Image]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_intro_image_with_http_info(**kwargs)
        else:
            (data) = self.get_intro_image_with_http_info(**kwargs)
            return data

    def get_intro_image_with_http_info(self, **kwargs):
        """
        Get introduction image
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_intro_image_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Image]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_intro_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/widgets/intro/images'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='list[Image]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_manufacturer_cover_image(self, manufacturer_id, **kwargs):
        """
        Get cover image of a manufacturer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_manufacturer_cover_image(manufacturer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int manufacturer_id: ID of the manufacturer to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_manufacturer_cover_image_with_http_info(manufacturer_id, **kwargs)
        else:
            (data) = self.get_manufacturer_cover_image_with_http_info(manufacturer_id, **kwargs)
            return data

    def get_manufacturer_cover_image_with_http_info(self, manufacturer_id, **kwargs):
        """
        Get cover image of a manufacturer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_manufacturer_cover_image_with_http_info(manufacturer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int manufacturer_id: ID of the manufacturer to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manufacturer_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manufacturer_cover_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'manufacturer_id' is set
        if ('manufacturer_id' not in params) or (params['manufacturer_id'] is None):
            raise ValueError("Missing the required parameter `manufacturer_id` when calling `get_manufacturer_cover_image`")


        collection_formats = {}

        resource_path = '/manufacturers/{manufacturer_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'manufacturer_id' in params:
            path_params['manufacturer_id'] = params['manufacturer_id']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_cover_image(self, product_id, **kwargs):
        """
        Get cover image of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_cover_image(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_cover_image_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_cover_image_with_http_info(product_id, **kwargs)
            return data

    def get_product_cover_image_with_http_info(self, product_id, **kwargs):
        """
        Get cover image of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_cover_image_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_cover_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_cover_image`")


        collection_formats = {}

        resource_path = '/products/{product_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_images(self, product_id, **kwargs):
        """
        Get images attached to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_images(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :param str type: type as screen_small or screen_large
        :param int page:
        :param int per_page:
        :return: ProductImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_images_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_images_with_http_info(product_id, **kwargs)
            return data

    def get_product_images_with_http_info(self, product_id, **kwargs):
        """
        Get images attached to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_images_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: ID of the product to fetch (required)
        :param str type: type as screen_small or screen_large
        :param int page:
        :param int per_page:
        :return: ProductImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'type', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_images" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_images`")


        collection_formats = {}

        resource_path = '/products/{product_id}/images'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
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
                                        response_type='ProductImagesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_slider_images(self, **kwargs):
        """
        Get introduction image
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_slider_images(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Image]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_slider_images_with_http_info(**kwargs)
        else:
            (data) = self.get_slider_images_with_http_info(**kwargs)
            return data

    def get_slider_images_with_http_info(self, **kwargs):
        """
        Get introduction image
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_slider_images_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Image]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_slider_images" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/widgets/slider/images'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='list[Image]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription_cover_image(self, subscription_id, **kwargs):
        """
        Get cover image of a subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_cover_image(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: ID of the subscription to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_cover_image_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_subscription_cover_image_with_http_info(subscription_id, **kwargs)
            return data

    def get_subscription_cover_image_with_http_info(self, subscription_id, **kwargs):
        """
        Get cover image of a subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_cover_image_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: ID of the subscription to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription_cover_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_subscription_cover_image`")


        collection_formats = {}

        resource_path = '/subscriptions/{subscription_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_supplier_cover_image(self, supplier_id, **kwargs):
        """
        Get cover image of a supplier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_supplier_cover_image(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int supplier_id: ID of the supplier to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_supplier_cover_image_with_http_info(supplier_id, **kwargs)
        else:
            (data) = self.get_supplier_cover_image_with_http_info(supplier_id, **kwargs)
            return data

    def get_supplier_cover_image_with_http_info(self, supplier_id, **kwargs):
        """
        Get cover image of a supplier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_supplier_cover_image_with_http_info(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int supplier_id: ID of the supplier to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supplier_cover_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params) or (params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `get_supplier_cover_image`")


        collection_formats = {}

        resource_path = '/suppliers/{supplier_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'supplier_id' in params:
            path_params['supplier_id'] = params['supplier_id']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_video_cover(self, video, **kwargs):
        """
        Get video cover
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_cover(video, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video: ID of the video to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_cover_with_http_info(video, **kwargs)
        else:
            (data) = self.get_video_cover_with_http_info(video, **kwargs)
            return data

    def get_video_cover_with_http_info(self, video, **kwargs):
        """
        Get video cover
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_cover_with_http_info(video, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video: ID of the video to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_cover" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video' is set
        if ('video' not in params) or (params['video'] is None):
            raise ValueError("Missing the required parameter `video` when calling `get_video_cover`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'video' in params:
            path_params['video'] = params['video']

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
