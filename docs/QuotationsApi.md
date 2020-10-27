# swagger_client.QuotationsApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotations_post**](QuotationsApi.md#quotations_post) | **POST** /quotations | Create A New Quotation
[**quotations_quotation_reference_get**](QuotationsApi.md#quotations_quotation_reference_get) | **GET** /quotations/{quotationReference} | View A Quotation

# **quotations_post**
> ResponseQuotation quotations_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create A New Quotation

Provided with a valid object representation, this endpoint allows for a new quotation to be created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotationsApi()
body = swagger_client.RequestQuotation() # RequestQuotation | Represents the request body of a Quotation.
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_correlation_id = 'x_correlation_id_example' # str | Header parameter to uniquely identify the request. Must be supplied as a UUID. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_user_bearer = 'x_user_bearer_example' # str | Used to pass user’s access token when OAuth 2.0/OIDC authorisation framework is used for end-user authentication (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)
x_content_hash = 'x_content_hash_example' # str | SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. (optional)
x_user_credential_1 = 'x_user_credential_1_example' # str | The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_user_credential_2 = 'x_user_credential_2_example' # str | The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_channel = 'x_channel_example' # str | String containing the channel that was used to originate the request. For example USSD, Web, App. (optional)
x_callback_url = 'x_callback_url_example' # str | The URL supplied by the client that will be used to return the callback in the form of a HTTP PUT. (optional)
x_account_holding_institution_identifier_type = 'x_account_holding_institution_identifier_type_example' # str | A header variable that identifies the type of the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier header. (optional)
x_account_holding_institution_identifier = 'x_account_holding_institution_identifier_example' # str | A header variable that identifies the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier-Type header. (optional)

try:
    # Create A New Quotation
    api_response = api_instance.quotations_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotationsApi->quotations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestQuotation**](RequestQuotation.md)| Represents the request body of a Quotation. | 
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_correlation_id** | **str**| Header parameter to uniquely identify the request. Must be supplied as a UUID. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_user_bearer** | **str**| Used to pass user’s access token when OAuth 2.0/OIDC authorisation framework is used for end-user authentication | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 
 **x_content_hash** | **str**| SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. | [optional] 
 **x_user_credential_1** | **str**| The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_user_credential_2** | **str**| The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_channel** | **str**| String containing the channel that was used to originate the request. For example USSD, Web, App. | [optional] 
 **x_callback_url** | **str**| The URL supplied by the client that will be used to return the callback in the form of a HTTP PUT. | [optional] 
 **x_account_holding_institution_identifier_type** | **str**| A header variable that identifies the type of the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier header. | [optional] 
 **x_account_holding_institution_identifier** | **str**| A header variable that identifies the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier-Type header. | [optional] 

### Return type

[**ResponseQuotation**](ResponseQuotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotations_quotation_reference_get**
> ResponseQuotation quotations_quotation_reference_get(quotation_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View A Quotation

This endpoint returns a specific quotation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotationsApi()
quotation_reference = 'quotation_reference_example' # str | Path variable to uniquely identify the quotation.
x_date = '2013-10-20T19:20:30+01:00' # datetime | Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as 'Date' in version 1.0 of the Mobile Money API. (optional)
x_api_key = 'x_api_key_example' # str | Used to pass pre-shared client's API key to the server. (optional)
x_user_bearer = 'x_user_bearer_example' # str | Used to pass user’s access token when OAuth 2.0/OIDC authorisation framework is used for end-user authentication (optional)
x_client_id = 'x_client_id_example' # str | Used to pass pre-shared client's identifier to the server. (optional)
x_content_hash = 'x_content_hash_example' # str | SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. (optional)
x_user_credential_1 = 'x_user_credential_1_example' # str | The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_user_credential_2 = 'x_user_credential_2_example' # str | The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. (optional)
x_channel = 'x_channel_example' # str | String containing the channel that was used to originate the request. For example USSD, Web, App. (optional)
x_account_holding_institution_identifier_type = 'x_account_holding_institution_identifier_type_example' # str | A header variable that identifies the type of the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier header. (optional)
x_account_holding_institution_identifier = 'x_account_holding_institution_identifier_example' # str | A header variable that identifies the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier-Type header. (optional)

try:
    # View A Quotation
    api_response = api_instance.quotations_quotation_reference_get(quotation_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotationsApi->quotations_quotation_reference_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quotation_reference** | **str**| Path variable to uniquely identify the quotation. | 
 **x_date** | **datetime**| Header parameter to indicate the date and time that the message was originated. It is used for basic message integrity checks, to ensure the request is not stale. Note that the header was previously referenced as &#x27;Date&#x27; in version 1.0 of the Mobile Money API. | [optional] 
 **x_api_key** | **str**| Used to pass pre-shared client&#x27;s API key to the server. | [optional] 
 **x_user_bearer** | **str**| Used to pass user’s access token when OAuth 2.0/OIDC authorisation framework is used for end-user authentication | [optional] 
 **x_client_id** | **str**| Used to pass pre-shared client&#x27;s identifier to the server. | [optional] 
 **x_content_hash** | **str**| SHA-256 hex digest of the request content (encrypted or plain). Applicable only if basic data integrity checking is to be performed. | [optional] 
 **x_user_credential_1** | **str**| The end-users encrypted security credential. Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_user_credential_2** | **str**| The end-users encrypted security credential Should only be used when OAuth 2.0/OIDC authorisation framework has not been implemented by the API Provider. | [optional] 
 **x_channel** | **str**| String containing the channel that was used to originate the request. For example USSD, Web, App. | [optional] 
 **x_account_holding_institution_identifier_type** | **str**| A header variable that identifies the type of the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier header. | [optional] 
 **x_account_holding_institution_identifier** | **str**| A header variable that identifies the account holding institution. This header is used to support request routing and should be used in conjunction with the X-Account-Holding-Institution-Identifier-Type header. | [optional] 

### Return type

[**ResponseQuotation**](ResponseQuotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

