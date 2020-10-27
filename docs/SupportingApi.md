# swagger_client.SupportingApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heartbeat_get**](SupportingApi.md#heartbeat_get) | **GET** /heartbeat | Check API availability
[**requeststates_server_correlation_id_get**](SupportingApi.md#requeststates_server_correlation_id_get) | **GET** /requeststates/{serverCorrelationId} | View A Request State
[**requeststates_server_correlation_id_patch**](SupportingApi.md#requeststates_server_correlation_id_patch) | **PATCH** /requeststates/{serverCorrelationId} | Update A Request State
[**responses_client_correlation_id_get**](SupportingApi.md#responses_client_correlation_id_get) | **GET** /responses/{clientCorrelationId} | View A Response

# **heartbeat_get**
> ResponseHeartbeat heartbeat_get(x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id)

Check API availability

This endpoint returns the current status of the API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportingApi()
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)

try:
    # Check API availability
    api_response = api_instance.heartbeat_get(x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportingApi->heartbeat_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 

### Return type

[**ResponseHeartbeat**](ResponseHeartbeat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeststates_server_correlation_id_get**
> RequestStateObject requeststates_server_correlation_id_get(server_correlation_id, x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)

View A Request State

This endpoint returns a specific request state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportingApi()
server_correlation_id = 'server_correlation_id_example' # str | Path variable to uniquely identify a request state. Must be supplied as a UUID.
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)
x_content_hash = 'x_content_hash_example' # str | SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. (optional)
x_user_credential_1 = 'x_user_credential_1_example' # str | The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_user_credential_2 = 'x_user_credential_2_example' # str | The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_channel = 'x_channel_example' # str | String containing the channel that was used to originate the request. For example USSD, Web, App. (optional)

try:
    # View A Request State
    api_response = api_instance.requeststates_server_correlation_id_get(server_correlation_id, x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportingApi->requeststates_server_correlation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_correlation_id** | **str**| Path variable to uniquely identify a request state. Must be supplied as a UUID. | 
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 
 **x_content_hash** | **str**| SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. | [optional] 
 **x_user_credential_1** | **str**| The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_user_credential_2** | **str**| The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_channel** | **str**| String containing the channel that was used to originate the request. For example USSD, Web, App. | [optional] 

### Return type

[**RequestStateObject**](RequestStateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeststates_server_correlation_id_patch**
> requeststates_server_correlation_id_patch(body, server_correlation_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)

Update A Request State

This endpoint updates a specific request state. This operation is to be deprecated. Please refer to Callback definitions for the revised approach to implementing asynchronous callbacks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportingApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
server_correlation_id = 'server_correlation_id_example' # str | Path variable to uniquely identify a request state. Must be supplied as a UUID.
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_correlation_id = 'x_correlation_id_example' # str | Header parameter to uniquely identify the request. Must be supplied as a UUID. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)
x_content_hash = 'x_content_hash_example' # str | SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. (optional)
x_user_credential_1 = 'x_user_credential_1_example' # str | The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_user_credential_2 = 'x_user_credential_2_example' # str | The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_channel = 'x_channel_example' # str | String containing the channel that was used to originate the request. For example USSD, Web, App. (optional)

try:
    # Update A Request State
    api_instance.requeststates_server_correlation_id_patch(body, server_correlation_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)
except ApiException as e:
    print("Exception when calling SupportingApi->requeststates_server_correlation_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **server_correlation_id** | **str**| Path variable to uniquely identify a request state. Must be supplied as a UUID. | 
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_correlation_id** | **str**| Header parameter to uniquely identify the request. Must be supplied as a UUID. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 
 **x_content_hash** | **str**| SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. | [optional] 
 **x_user_credential_1** | **str**| The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_user_credential_2** | **str**| The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_channel** | **str**| String containing the channel that was used to originate the request. For example USSD, Web, App. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **responses_client_correlation_id_get**
> ResponseResponse responses_client_correlation_id_get(client_correlation_id, x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)

View A Response

This endpoint returns a specific response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportingApi()
client_correlation_id = 'client_correlation_id_example' # str | Path variable to uniquely identify a response object. Must be supplied as a UUID.
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)
x_content_hash = 'x_content_hash_example' # str | SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. (optional)
x_user_credential_1 = 'x_user_credential_1_example' # str | The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_user_credential_2 = 'x_user_credential_2_example' # str | The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_channel = 'x_channel_example' # str | String containing the channel that was used to originate the request. For example USSD, Web, App. (optional)

try:
    # View A Response
    api_response = api_instance.responses_client_correlation_id_get(client_correlation_id, x_date=x_date, x_api_key=x_api_key, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportingApi->responses_client_correlation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_correlation_id** | **str**| Path variable to uniquely identify a response object. Must be supplied as a UUID. | 
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 
 **x_content_hash** | **str**| SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. | [optional] 
 **x_user_credential_1** | **str**| The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_user_credential_2** | **str**| The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_channel** | **str**| String containing the channel that was used to originate the request. For example USSD, Web, App. | [optional] 

### Return type

[**ResponseResponse**](ResponseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

