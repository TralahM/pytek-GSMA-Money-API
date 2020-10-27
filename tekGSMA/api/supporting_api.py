# coding: utf-8

"""
    Mobile Money API

    This document defines the RESTful endpoints provided by the GSMA Mobile Money API You can find out more about what the API can do for your business at [https://developer.mobilemoneyapi.io]   # noqa: E501

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SupportingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heartbeat_get(self, **kwargs):  # noqa: E501
        """Check API availability  # noqa: E501

        This endpoint returns the current status of the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heartbeat_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :return: ResponseHeartbeat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heartbeat_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heartbeat_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heartbeat_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check API availability  # noqa: E501

        This endpoint returns the current status of the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heartbeat_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :return: ResponseHeartbeat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_date', 'x_api_key', 'x_client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heartbeat_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_date' in params:
            header_params['X-Date'] = params['x_date']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-Key'] = params['x_api_key']  # noqa: E501
        if 'x_client_id' in params:
            header_params['X-Client-Id'] = params['x_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heartbeat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseHeartbeat',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def requeststates_server_correlation_id_get(self, server_correlation_id, **kwargs):  # noqa: E501
        """View A Request State  # noqa: E501

        This endpoint returns a specific request state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeststates_server_correlation_id_get(server_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_correlation_id: Path variable to uniquely identify a request state. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: RequestStateObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.requeststates_server_correlation_id_get_with_http_info(server_correlation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.requeststates_server_correlation_id_get_with_http_info(server_correlation_id, **kwargs)  # noqa: E501
            return data

    def requeststates_server_correlation_id_get_with_http_info(self, server_correlation_id, **kwargs):  # noqa: E501
        """View A Request State  # noqa: E501

        This endpoint returns a specific request state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeststates_server_correlation_id_get_with_http_info(server_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_correlation_id: Path variable to uniquely identify a request state. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: RequestStateObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_correlation_id', 'x_date', 'x_api_key', 'x_client_id', 'x_content_hash', 'x_user_credential_1', 'x_user_credential_2', 'x_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method requeststates_server_correlation_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_correlation_id' is set
        if ('server_correlation_id' not in params or
                params['server_correlation_id'] is None):
            raise ValueError("Missing the required parameter `server_correlation_id` when calling `requeststates_server_correlation_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_correlation_id' in params:
            path_params['serverCorrelationId'] = params['server_correlation_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_date' in params:
            header_params['X-Date'] = params['x_date']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-Key'] = params['x_api_key']  # noqa: E501
        if 'x_client_id' in params:
            header_params['X-Client-Id'] = params['x_client_id']  # noqa: E501
        if 'x_content_hash' in params:
            header_params['X-Content-Hash'] = params['x_content_hash']  # noqa: E501
        if 'x_user_credential_1' in params:
            header_params['X-User-Credential-1'] = params['x_user_credential_1']  # noqa: E501
        if 'x_user_credential_2' in params:
            header_params['X-User-Credential-2'] = params['x_user_credential_2']  # noqa: E501
        if 'x_channel' in params:
            header_params['X-Channel'] = params['x_channel']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/requeststates/{serverCorrelationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestStateObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def requeststates_server_correlation_id_patch(self, body, server_correlation_id, **kwargs):  # noqa: E501
        """Update A Request State  # noqa: E501

        This endpoint updates a specific request state. This operation is to be deprecated. Please refer to Callback definitions for the revised approach to implementing asynchronous callbacks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeststates_server_correlation_id_patch(body, server_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RequestGenericPatch] body: Represents the request body of a batch of generic Patch operation. (required)
        :param str server_correlation_id: Path variable to uniquely identify a request state. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_correlation_id: Header parameter to uniquely identify the request. Must be supplied as a UUID.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.requeststates_server_correlation_id_patch_with_http_info(body, server_correlation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.requeststates_server_correlation_id_patch_with_http_info(body, server_correlation_id, **kwargs)  # noqa: E501
            return data

    def requeststates_server_correlation_id_patch_with_http_info(self, body, server_correlation_id, **kwargs):  # noqa: E501
        """Update A Request State  # noqa: E501

        This endpoint updates a specific request state. This operation is to be deprecated. Please refer to Callback definitions for the revised approach to implementing asynchronous callbacks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeststates_server_correlation_id_patch_with_http_info(body, server_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RequestGenericPatch] body: Represents the request body of a batch of generic Patch operation. (required)
        :param str server_correlation_id: Path variable to uniquely identify a request state. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_correlation_id: Header parameter to uniquely identify the request. Must be supplied as a UUID.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'server_correlation_id', 'x_date', 'x_correlation_id', 'x_api_key', 'x_client_id', 'x_content_hash', 'x_user_credential_1', 'x_user_credential_2', 'x_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method requeststates_server_correlation_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `requeststates_server_correlation_id_patch`")  # noqa: E501
        # verify the required parameter 'server_correlation_id' is set
        if ('server_correlation_id' not in params or
                params['server_correlation_id'] is None):
            raise ValueError("Missing the required parameter `server_correlation_id` when calling `requeststates_server_correlation_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_correlation_id' in params:
            path_params['serverCorrelationId'] = params['server_correlation_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_date' in params:
            header_params['X-Date'] = params['x_date']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-CorrelationID'] = params['x_correlation_id']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-Key'] = params['x_api_key']  # noqa: E501
        if 'x_client_id' in params:
            header_params['X-Client-Id'] = params['x_client_id']  # noqa: E501
        if 'x_content_hash' in params:
            header_params['X-Content-Hash'] = params['x_content_hash']  # noqa: E501
        if 'x_user_credential_1' in params:
            header_params['X-User-Credential-1'] = params['x_user_credential_1']  # noqa: E501
        if 'x_user_credential_2' in params:
            header_params['X-User-Credential-2'] = params['x_user_credential_2']  # noqa: E501
        if 'x_channel' in params:
            header_params['X-Channel'] = params['x_channel']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/requeststates/{serverCorrelationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def responses_client_correlation_id_get(self, client_correlation_id, **kwargs):  # noqa: E501
        """View A Response  # noqa: E501

        This endpoint returns a specific response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.responses_client_correlation_id_get(client_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_correlation_id: Path variable to uniquely identify a response object. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: ResponseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.responses_client_correlation_id_get_with_http_info(client_correlation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.responses_client_correlation_id_get_with_http_info(client_correlation_id, **kwargs)  # noqa: E501
            return data

    def responses_client_correlation_id_get_with_http_info(self, client_correlation_id, **kwargs):  # noqa: E501
        """View A Response  # noqa: E501

        This endpoint returns a specific response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.responses_client_correlation_id_get_with_http_info(client_correlation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_correlation_id: Path variable to uniquely identify a response object. Must be supplied as a UUID. (required)
        :param datetime x_date: Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API.
        :param str x_api_key: Used to pass pre-shared client's API key to the server.
        :param str x_client_id: Used to pass pre-shared client's identifier to the server.
        :param str x_content_hash: SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed.
        :param str x_user_credential_1: The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_user_credential_2: The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider.
        :param str x_channel: String containing the channel that was used to originate the request. For example USSD, Web, App.
        :return: ResponseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_correlation_id', 'x_date', 'x_api_key', 'x_client_id', 'x_content_hash', 'x_user_credential_1', 'x_user_credential_2', 'x_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method responses_client_correlation_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_correlation_id' is set
        if ('client_correlation_id' not in params or
                params['client_correlation_id'] is None):
            raise ValueError("Missing the required parameter `client_correlation_id` when calling `responses_client_correlation_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_correlation_id' in params:
            path_params['clientCorrelationId'] = params['client_correlation_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_date' in params:
            header_params['X-Date'] = params['x_date']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-Key'] = params['x_api_key']  # noqa: E501
        if 'x_client_id' in params:
            header_params['X-Client-Id'] = params['x_client_id']  # noqa: E501
        if 'x_content_hash' in params:
            header_params['X-Content-Hash'] = params['x_content_hash']  # noqa: E501
        if 'x_user_credential_1' in params:
            header_params['X-User-Credential-1'] = params['x_user_credential_1']  # noqa: E501
        if 'x_user_credential_2' in params:
            header_params['X-User-Credential-2'] = params['x_user_credential_2']  # noqa: E501
        if 'x_channel' in params:
            header_params['X-Channel'] = params['x_channel']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/responses/{clientCorrelationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
