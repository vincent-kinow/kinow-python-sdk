# kaemo_client
Public api for Kaemo back office

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build date: 2018-03-19T13:44:20.451Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kaemo_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kaemo_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = kaemo_client.AccessesApi()
customer_id = 789 # int | ID of the customer to fetch (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try:
    api_response = api_instance.get_available_categories(customer_id=customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessesApi->get_available_categories: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.kinow.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessesApi* | [**get_available_categories**](#get_available_categories) | **GET** /categories-accesses | 
*AccessesApi* | [**get_available_category**](#get_available_category) | **GET** /categories-accesses/{category_id} | 
*AccessesApi* | [**get_customer_has_access_to_product**](#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*AccessesApi* | [**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*AccessesApi* | [**get_product_availability**](#get_product_availability) | **GET** /products/{product_id}/access | 
*ActorsApi* | [**get_actor**](#get_actor) | **GET** /actors/{actor_id} | 
*ActorsApi* | [**get_actors**](#get_actors) | **GET** /actors | 
*ActorsApi* | [**get_product_actors**](#get_product_actors) | **GET** /products/{product_id}/actors | 
*AddressApi* | [**get_customer_address**](#get_customer_address) | **GET** /customers/{customer_id}/address | 
*AddressApi* | [**update_address**](#update_address) | **PUT** /addresses/{address_id} | 
*AttributesApi* | [**create_product_attribute**](#create_product_attribute) | **POST** /attributes | 
*AttributesApi* | [**get_product_attributes**](#get_product_attributes) | **GET** /products/{product_id}/attributes | 
*AttributesApi* | [**update_product_attribute**](#update_product_attribute) | **PUT** /attributes/{attribute_id} | 
*BookmarksApi* | [**attach_bookmark_to_customer**](#attach_bookmark_to_customer) | **POST** /customers/{customer_id}/bookmarks | 
*BookmarksApi* | [**detach_bookmark_from_customer**](#detach_bookmark_from_customer) | **DELETE** /customers/{customer_id}/bookmarks/{product_id} | 
*BookmarksApi* | [**get_customer_bookmarks**](#get_customer_bookmarks) | **GET** /customers/{customer_id}/bookmarks | 
*CMSCategoriesApi* | [**create_cms_category**](#create_cms_category) | **POST** /cms-categories | 
*CMSCategoriesApi* | [**get_cms_categories**](#get_cms_categories) | **GET** /cms-categories | 
*CMSCategoriesApi* | [**update_cms_category**](#update_cms_category) | **PUT** /cms-categories/{cms_category_id} | 
*CMSPagesApi* | [**create_cms_page**](#create_cms_page) | **POST** /cms-pages | 
*CMSPagesApi* | [**get_cms_pages**](#get_cms_pages) | **GET** /cms-pages | 
*CMSPagesApi* | [**update_cms_page**](#update_cms_page) | **PUT** /cms-pages/{cms_page_id} | 
*CartRulesApi* | [**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
*CartRulesApi* | [**create_cart_rule**](#create_cart_rule) | **POST** /cart-rules | 
*CartRulesApi* | [**delete_cart_rule**](#delete_cart_rule) | **DELETE** /cart-rules/{cart_rule_id} | 
*CartRulesApi* | [**get_cart_rule**](#get_cart_rule) | **GET** /cart-rules/{cart_rule_id} | 
*CartRulesApi* | [**get_cart_rules**](#get_cart_rules) | **GET** /cart-rules | 
*CartRulesApi* | [**update_cart_rule**](#update_cart_rule) | **PUT** /cart-rules/{cart_rule_id} | 
*CartsApi* | [**add_product_to_cart**](#add_product_to_cart) | **POST** /carts/{cart_id}/products | 
*CartsApi* | [**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
*CartsApi* | [**attach_cart_to_customer**](#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
*CartsApi* | [**create_cart**](#create_cart) | **POST** /carts | 
*CartsApi* | [**delete_cart**](#delete_cart) | **DELETE** /carts/{cart_id} | 
*CartsApi* | [**delete_product_from_cart**](#delete_product_from_cart) | **DELETE** /carts/{cart_id}/products | 
*CartsApi* | [**get_cart**](#get_cart) | **GET** /carts/{cart_id} | 
*CartsApi* | [**get_customer_carts**](#get_customer_carts) | **GET** /customers/{customer_id}/carts | 
*CartsApi* | [**get_last_cart**](#get_last_cart) | **GET** /customers/{customer_id}/last-cart | 
*CartsApi* | [**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
*CartsApi* | [**update_cart**](#update_cart) | **PUT** /carts/{cart_id} | 
*CartsApi* | [**validate_cart**](#validate_cart) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 
*CartsApi* | [**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
*CategoriesApi* | [**create_category**](#create_category) | **POST** /categories | 
*CategoriesApi* | [**get_available_categories**](#get_available_categories) | **GET** /categories-accesses | 
*CategoriesApi* | [**get_available_category**](#get_available_category) | **GET** /categories-accesses/{category_id} | 
*CategoriesApi* | [**get_categories**](#get_categories) | **GET** /categories | 
*CategoriesApi* | [**get_categories_from_category**](#get_categories_from_category) | **GET** /categories/{category_id}/categories | 
*CategoriesApi* | [**get_category**](#get_category) | **GET** /categories/{category_id} | 
*CategoriesApi* | [**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
*CategoriesApi* | [**get_category_features**](#get_category_features) | **GET** /categories/{category_id}/features | 
*CategoriesApi* | [**get_category_products**](#get_category_products) | **GET** /categories/{category_id}/products | 
*CategoriesApi* | [**get_product_categories**](#get_product_categories) | **GET** /products/{product_id}/categories | 
*CategoriesApi* | [**get_subscription_categories**](#get_subscription_categories) | **GET** /subscriptions/{subscription_id}/categories | 
*CountriesApi* | [**get_countries**](#get_countries) | **GET** /countries | 
*CurrenciesApi* | [**get_currencies**](#get_currencies) | **GET** /currencies | 
*CustomerThreadsApi* | [**get_customer_thread**](#get_customer_thread) | **GET** /customer-threads/{customer_thread_id} | 
*CustomerThreadsApi* | [**get_customer_threads**](#get_customer_threads) | **GET** /customer-threads | 
*CustomersApi* | [**attach_cart_to_customer**](#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
*CustomersApi* | [**check_customer_credentials**](#check_customer_credentials) | **POST** /customers/check-credentials | 
*CustomersApi* | [**create_customer**](#create_customer) | **POST** /customers | 
*CustomersApi* | [**create_facebook_id**](#create_facebook_id) | **POST** /facebook/customers | 
*CustomersApi* | [**delete_customer**](#delete_customer) | **DELETE** /customers/{customer_id} | 
*CustomersApi* | [**generate_authentication_token**](#generate_authentication_token) | **GET** /customers/{customer_id}/authentication-token | 
*CustomersApi* | [**get_customer**](#get_customer) | **GET** /customers/{customer_id} | 
*CustomersApi* | [**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
*CustomersApi* | [**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
*CustomersApi* | [**get_customer_address**](#get_customer_address) | **GET** /customers/{customer_id}/address | 
*CustomersApi* | [**get_customer_current_views**](#get_customer_current_views) | **GET** /customers/{customer_id}/current-views | 
*CustomersApi* | [**get_customer_has_access_to_product**](#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*CustomersApi* | [**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*CustomersApi* | [**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
*CustomersApi* | [**get_customers**](#get_customers) | **GET** /customers | 
*CustomersApi* | [**get_download_url**](#get_download_url) | **GET** /customers/{customer_id}/videos/{video_id}/download | 
*CustomersApi* | [**get_marlin_token**](#get_marlin_token) | **GET** /customers/{customer_id}/videos/{video_id}/marlin | 
*CustomersApi* | [**get_payment_customer_id**](#get_payment_customer_id) | **GET** /customers/{customer_id}/payments/{payment_name}/customer | 
*CustomersApi* | [**get_player_url**](#get_player_url) | **GET** /customers/{customer_id}/videos/{video_id}/player | 
*CustomersApi* | [**update_customer**](#update_customer) | **PUT** /customers/{customer_id} | 
*DirectorsApi* | [**get_director**](#get_director) | **GET** /directors/{director_id} | 
*DirectorsApi* | [**get_directors**](#get_directors) | **GET** /directors | 
*DirectorsApi* | [**get_product_directors**](#get_product_directors) | **GET** /products/{product_id}/directors | 
*ExtractsApi* | [**create_extract**](#create_extract) | **POST** /extracts | 
*ExtractsApi* | [**delete_extract**](#delete_extract) | **DELETE** /extracts/{extract_id} | 
*ExtractsApi* | [**get_extract_player**](#get_extract_player) | **GET** /extracts/{extract_id}/player | 
*ExtractsApi* | [**get_product_extracts**](#get_product_extracts) | **GET** /products/{product_id}/extracts | 
*ExtractsApi* | [**update_extract**](#update_extract) | **PUT** /extracts/{extract_id} | 
*FacebookApi* | [**create_facebook_id**](#create_facebook_id) | **POST** /facebook/customers | 
*FacebookApi* | [**get_facebook_customer**](#get_facebook_customer) | **GET** /facebook/customers/{facebook_id} | 
*FeatureValuesApi* | [**attach_features_to_product**](#attach_features_to_product) | **POST** /products/{product_id}/features | 
*FeatureValuesApi* | [**attach_features_to_video**](#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*FeatureValuesApi* | [**detach_feature_to_product**](#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*FeatureValuesApi* | [**get_feature_values**](#get_feature_values) | **GET** /feature-values | 
*FeaturesApi* | [**attach_features_to_product**](#attach_features_to_product) | **POST** /products/{product_id}/features | 
*FeaturesApi* | [**attach_features_to_video**](#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*FeaturesApi* | [**detach_feature_to_product**](#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*FeaturesApi* | [**get_category_features**](#get_category_features) | **GET** /categories/{category_id}/features | 
*FeaturesApi* | [**get_feature_values**](#get_feature_values) | **GET** /feature-values | 
*FeaturesApi* | [**get_features**](#get_features) | **GET** /features | 
*FeaturesApi* | [**get_product_features**](#get_product_features) | **GET** /products/{product_id}/features | 
*FeaturesApi* | [**get_video_features**](#get_video_features) | **GET** /videos/{video_id}/features | 
*GendersApi* | [**get_genders**](#get_genders) | **GET** /genders | 
*GeolocationsApi* | [**geolocations**](#geolocations) | **POST** /geolocations | 
*GeolocationsApi* | [**get_product_geolocations**](#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**get_product_geolocations_by_ip**](#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**get_video_geolocation**](#get_video_geolocation) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
*GeolocationsApi* | [**set_product_geolocation**](#set_product_geolocation) | **PUT** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**set_video_geolocation**](#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 
*GroupsApi* | [**attach_customer_to_group**](#attach_customer_to_group) | **POST** /groups/{group_id}/customers | 
*GroupsApi* | [**detach_customer_from_group**](#detach_customer_from_group) | **DELETE** /groups/{group_id}/customers/{customer_id} | 
*GroupsApi* | [**get_groups**](#get_groups) | **GET** /groups | 
*ImagesApi* | [**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
*ImagesApi* | [**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
*ImagesApi* | [**get_manufacturer_cover_image**](#get_manufacturer_cover_image) | **GET** /manufacturers/{manufacturer_id}/cover | 
*ImagesApi* | [**get_product_cover_image**](#get_product_cover_image) | **GET** /products/{product_id}/cover | 
*ImagesApi* | [**get_product_images**](#get_product_images) | **GET** /products/{product_id}/images | 
*ImagesApi* | [**get_slider_images**](#get_slider_images) | **GET** /widgets/slider/images | 
*ImagesApi* | [**get_subscription_cover_image**](#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
*ImagesApi* | [**get_supplier_cover_image**](#get_supplier_cover_image) | **GET** /suppliers/{supplier_id}/cover | 
*ImagesApi* | [**get_video_cover**](#get_video_cover) | **GET** /videos/{video_id}/cover | 
*LanguagesApi* | [**get_languages**](#get_languages) | **GET** /languages | 
*ManufacturersApi* | [**get_manufacturer_cover_image**](#get_manufacturer_cover_image) | **GET** /manufacturers/{manufacturer_id}/cover | 
*MediaFilesApi* | [**get_media_source_files**](#get_media_source_files) | **GET** /media-sources/{source_id}/files | 
*MediaFilesApi* | [**post_media_source_files**](#post_media_source_files) | **POST** /media-sources/{source_id}/files | 
*MediaSourcesApi* | [**get_media_source**](#get_media_source) | **GET** /media-sources/{source_id} | 
*MediaSourcesApi* | [**get_media_source_files**](#get_media_source_files) | **GET** /media-sources/{source_id}/files | 
*MediaSourcesApi* | [**get_media_sources**](#get_media_sources) | **GET** /media-sources | 
*MediaSourcesApi* | [**post_media_source_files**](#post_media_source_files) | **POST** /media-sources/{source_id}/files | 
*OAuthApi* | [**get_token**](#get_token) | **POST** /get-token | 
*OrderHistoriesApi* | [**get_order_histories**](#get_order_histories) | **GET** /orders/{order_id}/histories | 
*OrderStatesApi* | [**get_order_state**](#get_order_state) | **GET** /order-states/{order_state_id} | 
*OrderStatesApi* | [**get_order_states**](#get_order_states) | **GET** /order-states | 
*OrdersApi* | [**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
*OrdersApi* | [**get_order**](#get_order) | **GET** /orders/{order_id} | 
*OrdersApi* | [**get_order_histories**](#get_order_histories) | **GET** /orders/{order_id}/histories | 
*OrdersApi* | [**get_order_invoice**](#get_order_invoice) | **GET** /orders/{order_id}/invoice | 
*PaymentModulesApi* | [**get_payment_modules**](#get_payment_modules) | **GET** /payment-modules | 
*PaymentModulesApi* | [**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
*PaymentModulesApi* | [**validate_cart**](#validate_cart) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 
*PaymentModulesApi* | [**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
*PlayerApi* | [**get_extract_player**](#get_extract_player) | **GET** /extracts/{extract_id}/player | 
*ProductAccessesApi* | [**create_product_access**](#create_product_access) | **POST** /product-accesses | 
*ProductAccessesApi* | [**delete_product_access**](#delete_product_access) | **DELETE** /product-accesses/{product_access_id} | 
*ProductAccessesApi* | [**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
*ProductAccessesApi* | [**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
*ProductAccessesApi* | [**get_product_access**](#get_product_access) | **GET** /product-accesses/{product_access_id} | 
*ProductAccessesApi* | [**get_product_accesses**](#get_product_accesses) | **GET** /product-accesses | 
*ProductAccessesApi* | [**stop_subscription**](#stop_subscription) | **PUT** /customers/{customer_id}/unsubscribe | 
*ProductAccessesApi* | [**update_product_access**](#update_product_access) | **PUT** /product-accesses/{product_access_id} | 
*ProductsApi* | [**attach_features_to_product**](#attach_features_to_product) | **POST** /products/{product_id}/features | 
*ProductsApi* | [**attach_product_to_category**](#attach_product_to_category) | **POST** /products/{product_id}/categories | 
*ProductsApi* | [**attach_video_to_product**](#attach_video_to_product) | **POST** /products/{product_id}/videos | 
*ProductsApi* | [**create_product**](#create_product) | **POST** /products | 
*ProductsApi* | [**delete_product**](#delete_product) | **DELETE** /products/{product_id} | 
*ProductsApi* | [**detach_feature_to_product**](#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*ProductsApi* | [**detach_product_from_category**](#detach_product_from_category) | **DELETE** /products/{product_id}/categories/{category_id} | 
*ProductsApi* | [**get_category_products**](#get_category_products) | **GET** /categories/{category_id}/products | 
*ProductsApi* | [**get_customer_has_access_to_product**](#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*ProductsApi* | [**get_product**](#get_product) | **GET** /products/{product_id} | 
*ProductsApi* | [**get_product_actors**](#get_product_actors) | **GET** /products/{product_id}/actors | 
*ProductsApi* | [**get_product_attributes**](#get_product_attributes) | **GET** /products/{product_id}/attributes | 
*ProductsApi* | [**get_product_availability**](#get_product_availability) | **GET** /products/{product_id}/access | 
*ProductsApi* | [**get_product_categories**](#get_product_categories) | **GET** /products/{product_id}/categories | 
*ProductsApi* | [**get_product_cover_image**](#get_product_cover_image) | **GET** /products/{product_id}/cover | 
*ProductsApi* | [**get_product_directors**](#get_product_directors) | **GET** /products/{product_id}/directors | 
*ProductsApi* | [**get_product_extracts**](#get_product_extracts) | **GET** /products/{product_id}/extracts | 
*ProductsApi* | [**get_product_features**](#get_product_features) | **GET** /products/{product_id}/features | 
*ProductsApi* | [**get_product_geolocations**](#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
*ProductsApi* | [**get_product_geolocations_by_ip**](#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations | 
*ProductsApi* | [**get_product_images**](#get_product_images) | **GET** /products/{product_id}/images | 
*ProductsApi* | [**get_products**](#get_products) | **GET** /products | 
*ProductsApi* | [**get_products_from_product**](#get_products_from_product) | **GET** /products/{product_id}/products | 
*ProductsApi* | [**get_videos_from_product**](#get_videos_from_product) | **GET** /products/{product_id}/videos | 
*ProductsApi* | [**search_products**](#search_products) | **GET** /products/search/{search_query} | 
*ProductsApi* | [**set_product_geolocation**](#set_product_geolocation) | **PUT** /products/{product_id}/geolocations | 
*ProductsApi* | [**update_product**](#update_product) | **PUT** /products/{product_id} | 
*SubscriptionsApi* | [**get_disabled_subscriptions**](#get_disabled_subscriptions) | **GET** /videos/{video_id}/disabled-subscriptions | 
*SubscriptionsApi* | [**get_subscription**](#get_subscription) | **GET** /subscriptions/{subscription_id} | 
*SubscriptionsApi* | [**get_subscription_categories**](#get_subscription_categories) | **GET** /subscriptions/{subscription_id}/categories | 
*SubscriptionsApi* | [**get_subscription_cover_image**](#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
*SubscriptionsApi* | [**get_subscriptions**](#get_subscriptions) | **GET** /subscriptions | 
*SuppliersApi* | [**get_supplier_cover_image**](#get_supplier_cover_image) | **GET** /suppliers/{supplier_id}/cover | 
*VideosApi* | [**attach_features_to_video**](#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*VideosApi* | [**attach_video_to_product**](#attach_video_to_product) | **POST** /products/{product_id}/videos | 
*VideosApi* | [**create_video**](#create_video) | **POST** /videos | 
*VideosApi* | [**delete_video**](#delete_video) | **DELETE** /videos/{video_id} | 
*VideosApi* | [**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*VideosApi* | [**get_disabled_subscriptions**](#get_disabled_subscriptions) | **GET** /videos/{video_id}/disabled-subscriptions | 
*VideosApi* | [**get_download_url**](#get_download_url) | **GET** /customers/{customer_id}/videos/{video_id}/download | 
*VideosApi* | [**get_marlin_token**](#get_marlin_token) | **GET** /customers/{customer_id}/videos/{video_id}/marlin | 
*VideosApi* | [**get_player_url**](#get_player_url) | **GET** /customers/{customer_id}/videos/{video_id}/player | 
*VideosApi* | [**get_video**](#get_video) | **GET** /videos/{video_id} | 
*VideosApi* | [**get_video_access**](#get_video_access) | **GET** /videos/{video_id}/customers/{customer_id}/access | 
*VideosApi* | [**get_video_features**](#get_video_features) | **GET** /videos/{video_id}/features | 
*VideosApi* | [**get_video_geolocation**](#get_video_geolocation) | **GET** /videos/{video_id}/geolocation | 
*VideosApi* | [**get_video_geolocation_0**](#get_video_geolocation_0) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
*VideosApi* | [**get_video_player_url**](#get_video_player_url) | **GET** /videos/{video_id}/player | 
*VideosApi* | [**get_video_views**](#get_video_views) | **GET** /videos/{video_id}/views | 
*VideosApi* | [**get_videos**](#get_videos) | **GET** /videos | 
*VideosApi* | [**get_videos_from_product**](#get_videos_from_product) | **GET** /products/{product_id}/videos | 
*VideosApi* | [**set_video_geolocation**](#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 
*VideosApi* | [**update_video**](#update_video) | **PUT** /videos/{video_id} | 
*WidgetsApi* | [**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
*WidgetsApi* | [**get_slider_images**](#get_slider_images) | **GET** /widgets/slider/images | 


## Documentation For Models

 - [Actor](#Actor)
 - [Actors](#Actors)
 - [Address](#Address)
 - [BlogCategory](#BlogCategory)
 - [BlogPage](#BlogPage)
 - [CMSCategoriesLists](#CMSCategoriesLists)
 - [CMSCategory](#CMSCategory)
 - [CMSPage](#CMSPage)
 - [CMSPageLists](#CMSPageLists)
 - [Cart](#Cart)
 - [CartBody](#CartBody)
 - [CartRule](#CartRule)
 - [CartRuleRestrictionGroup](#CartRuleRestrictionGroup)
 - [CartRuleRestrictionGroupItem](#CartRuleRestrictionGroupItem)
 - [CartRules](#CartRules)
 - [Carts](#Carts)
 - [Categories](#Categories)
 - [Category](#Category)
 - [Countries](#Countries)
 - [Country](#Country)
 - [Currencies](#Currencies)
 - [Currency](#Currency)
 - [Customer](#Customer)
 - [CustomerCreateRequest](#CustomerCreateRequest)
 - [CustomerCurrentViews](#CustomerCurrentViews)
 - [CustomerId](#CustomerId)
 - [CustomerThread](#CustomerThread)
 - [CustomerThread1](#CustomerThread1)
 - [Customers](#Customers)
 - [Director](#Director)
 - [Director1](#Director1)
 - [DownloadUrl](#DownloadUrl)
 - [Extract](#Extract)
 - [Feature](#Feature)
 - [FeatureValue](#FeatureValue)
 - [Features](#Features)
 - [Gender](#Gender)
 - [Genders](#Genders)
 - [Geoloc](#Geoloc)
 - [Geolocs](#Geolocs)
 - [Group](#Group)
 - [Groups](#Groups)
 - [I18nField](#I18nField)
 - [Image](#Image)
 - [Language](#Language)
 - [Languages](#Languages)
 - [MarlinToken](#MarlinToken)
 - [MediaFile](#MediaFile)
 - [MediaFiles](#MediaFiles)
 - [MediaSource](#MediaSource)
 - [MediaSources](#MediaSources)
 - [OAuthToken](#OAuthToken)
 - [Order](#Order)
 - [OrderHistories](#OrderHistories)
 - [OrderHistory](#OrderHistory)
 - [OrderState](#OrderState)
 - [OrderStates](#OrderStates)
 - [Orders](#Orders)
 - [Pagination](#Pagination)
 - [PaymentArguments](#PaymentArguments)
 - [PaymentModule](#PaymentModule)
 - [PaymentModules](#PaymentModules)
 - [PaymentUrl](#PaymentUrl)
 - [PlayerConfiguration](#PlayerConfiguration)
 - [Product](#Product)
 - [ProductAccess](#ProductAccess)
 - [ProductAttribute](#ProductAttribute)
 - [ProductAttributeCreateRequest](#ProductAttributeCreateRequest)
 - [ProductAttributeUpdateRequest](#ProductAttributeUpdateRequest)
 - [ProductAttributesResponse](#ProductAttributesResponse)
 - [ProductExtractsResponse](#ProductExtractsResponse)
 - [ProductImagesResponse](#ProductImagesResponse)
 - [Products](#Products)
 - [Products1](#Products1)
 - [Subscription](#Subscription)
 - [SubscriptionAccesses](#SubscriptionAccesses)
 - [Subscriptions](#Subscriptions)
 - [Tag](#Tag)
 - [Video](#Video)
 - [VideoUrl](#VideoUrl)
 - [VideoViews](#VideoViews)
 - [Videos](#Videos)

