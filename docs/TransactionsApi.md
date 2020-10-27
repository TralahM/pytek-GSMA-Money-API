# swagger_client.TransactionsApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchtransactions_batch_id_completions_get**](TransactionsApi.md#batchtransactions_batch_id_completions_get) | **GET** /batchtransactions/{batchId}/completions | View Batch Completions
[**batchtransactions_batch_id_get**](TransactionsApi.md#batchtransactions_batch_id_get) | **GET** /batchtransactions/{batchId} | View A Transaction Batch
[**batchtransactions_batch_id_patch**](TransactionsApi.md#batchtransactions_batch_id_patch) | **PATCH** /batchtransactions/{batchId} | Update A Transaction Batch
[**batchtransactions_batch_id_rejections_get**](TransactionsApi.md#batchtransactions_batch_id_rejections_get) | **GET** /batchtransactions/{batchId}/rejections | View Batch Rejections
[**batchtransactions_post**](TransactionsApi.md#batchtransactions_post) | **POST** /batchtransactions | Create A Transaction Batch
[**transactions_post**](TransactionsApi.md#transactions_post) | **POST** /transactions | Create a Transaction
[**transactions_transaction_reference_get**](TransactionsApi.md#transactions_transaction_reference_get) | **GET** /transactions/{transactionReference} | View A Transaction
[**transactions_transaction_reference_reversals_post**](TransactionsApi.md#transactions_transaction_reference_reversals_post) | **POST** /transactions/{transactionReference}/reversals | Create A Reversal
[**transactionstypetransaction_type_put**](TransactionsApi.md#transactionstypetransaction_type_put) | **POST** /transactions/type/{transactionType} | Create a Transaction

# **batchtransactions_batch_id_completions_get**
> list[ResponseBatchTransactionCompletion] batchtransactions_batch_id_completions_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time)

View Batch Completions

This endpoint returns completed transactions for a specific batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
batch_id = 'batch_id_example' # str | Path variable to uniquely identify the transaction batch.
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
limit = 56 # int | Supports pagination. If this is not supplied, then the server will apply a limit of 50 records returned for each request. (optional)
offset = 56 # int | Supports pagination. This value will indicate the cursor position from where to retrieve the set of records. For example, a limit of 50 and offset of 10 will return records 11 to 60. (optional)
from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Indicates the minimum date for which records should be returned. (optional)
to_date_time = '2013-10-20T19:20:30+01:00' # datetime | Indicates the maximum date for which records should be returned. (optional)

try:
    # View Batch Completions
    api_response = api_instance.batchtransactions_batch_id_completions_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batchtransactions_batch_id_completions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Path variable to uniquely identify the transaction batch. | 
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
 **limit** | **int**| Supports pagination. If this is not supplied, then the server will apply a limit of 50 records returned for each request. | [optional] 
 **offset** | **int**| Supports pagination. This value will indicate the cursor position from where to retrieve the set of records. For example, a limit of 50 and offset of 10 will return records 11 to 60. | [optional] 
 **from_date_time** | **datetime**| Indicates the minimum date for which records should be returned. | [optional] 
 **to_date_time** | **datetime**| Indicates the maximum date for which records should be returned. | [optional] 

### Return type

[**list[ResponseBatchTransactionCompletion]**](ResponseBatchTransactionCompletion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batchtransactions_batch_id_get**
> ResponseBatchTransaction batchtransactions_batch_id_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View A Transaction Batch

This endpoint returns the current status of a batch transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
batch_id = 'batch_id_example' # str | Path variable to uniquely identify the transaction batch.
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
    # View A Transaction Batch
    api_response = api_instance.batchtransactions_batch_id_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batchtransactions_batch_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Path variable to uniquely identify the transaction batch. | 
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

[**ResponseBatchTransaction**](ResponseBatchTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batchtransactions_batch_id_patch**
> RequestStateObject batchtransactions_batch_id_patch(body, batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)

Update A Transaction Batch

This endpoint updates a specific transaction batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
batch_id = 'batch_id_example' # str | Path variable to uniquely identify the transaction batch.
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
x_correlation_id = 'x_correlation_id_example' # str | Header parameter to uniquely identify the request. Must be supplied as a UUID. (optional)

try:
    # Update A Transaction Batch
    api_response = api_instance.batchtransactions_batch_id_patch(body, batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batchtransactions_batch_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **batch_id** | **str**| Path variable to uniquely identify the transaction batch. | 
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
 **x_correlation_id** | **str**| Header parameter to uniquely identify the request. Must be supplied as a UUID. | [optional] 

### Return type

[**RequestStateObject**](RequestStateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batchtransactions_batch_id_rejections_get**
> list[ResponseBatchTransactionRejection] batchtransactions_batch_id_rejections_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time)

View Batch Rejections

This endpoint returns rejected transactions for a specific batch\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
batch_id = 'batch_id_example' # str | Path variable to uniquely identify the transaction batch.
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
limit = 56 # int | Supports pagination. If this is not supplied, then the server will apply a limit of 50 records returned for each request. (optional)
offset = 56 # int | Supports pagination. This value will indicate the cursor position from where to retrieve the set of records. For example, a limit of 50 and offset of 10 will return records 11 to 60. (optional)
from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Indicates the minimum date for which records should be returned. (optional)
to_date_time = '2013-10-20T19:20:30+01:00' # datetime | Indicates the maximum date for which records should be returned. (optional)

try:
    # View Batch Rejections
    api_response = api_instance.batchtransactions_batch_id_rejections_get(batch_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batchtransactions_batch_id_rejections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Path variable to uniquely identify the transaction batch. | 
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
 **limit** | **int**| Supports pagination. If this is not supplied, then the server will apply a limit of 50 records returned for each request. | [optional] 
 **offset** | **int**| Supports pagination. This value will indicate the cursor position from where to retrieve the set of records. For example, a limit of 50 and offset of 10 will return records 11 to 60. | [optional] 
 **from_date_time** | **datetime**| Indicates the minimum date for which records should be returned. | [optional] 
 **to_date_time** | **datetime**| Indicates the maximum date for which records should be returned. | [optional] 

### Return type

[**list[ResponseBatchTransactionRejection]**](ResponseBatchTransactionRejection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batchtransactions_post**
> RequestStateObject batchtransactions_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create A Transaction Batch

Provided with a valid object representation, this endpoint allows for a new transaction batch to be created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = swagger_client.RequestBatchTransaction() # RequestBatchTransaction | Represents the request body of a batch of transactions.
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
    # Create A Transaction Batch
    api_response = api_instance.batchtransactions_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batchtransactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBatchTransaction**](RequestBatchTransaction.md)| Represents the request body of a batch of transactions. | 
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

[**RequestStateObject**](RequestStateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_post**
> ResponseTransaction transactions_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create a Transaction

Provided with a valid object representation, this endpoint allows for a new transaction to be created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = swagger_client.RequestTransaction() # RequestTransaction | Represents the request body of a transaction.
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
    # Create a Transaction
    api_response = api_instance.transactions_post(body, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestTransaction**](RequestTransaction.md)| Represents the request body of a transaction. | 
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

[**ResponseTransaction**](ResponseTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_reference_get**
> ResponseTransaction transactions_transaction_reference_get(transaction_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View A Transaction

This endpoint returns the details of a transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
transaction_reference = 'transaction_reference_example' # str | Path variable to uniquely identify the transaction.
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
    # View A Transaction
    api_response = api_instance.transactions_transaction_reference_get(transaction_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_transaction_reference_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_reference** | **str**| Path variable to uniquely identify the transaction. | 
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

[**ResponseTransaction**](ResponseTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_reference_reversals_post**
> ResponseReversal transactions_transaction_reference_reversals_post(body, transaction_reference, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create A Reversal

Provided with a valid object representation, this endpoint allows for a new reversal to be created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = swagger_client.RequestReversal() # RequestReversal | Represents the request body of a transaction reversal.
transaction_reference = 'transaction_reference_example' # str | Path variable to uniquely identify the transaction.
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
    # Create A Reversal
    api_response = api_instance.transactions_transaction_reference_reversals_post(body, transaction_reference, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_transaction_reference_reversals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestReversal**](RequestReversal.md)| Represents the request body of a transaction reversal. | 
 **transaction_reference** | **str**| Path variable to uniquely identify the transaction. | 
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

[**ResponseReversal**](ResponseReversal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactionstypetransaction_type_put**
> ResponseTransactionType transactionstypetransaction_type_put(body, transaction_type, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create a Transaction

Provided with a valid object representation, this endpoint allows for a new transaction to be created for a given transaction type passed via the URL.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
body = NULL # object | Represents the request body of a transaction without Type.
transaction_type = 'transaction_type_example' # str | Identifies the type of transaction that is to be created.
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
    # Create a Transaction
    api_response = api_instance.transactionstypetransaction_type_put(body, transaction_type, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactionstypetransaction_type_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Represents the request body of a transaction without Type. | 
 **transaction_type** | **str**| Identifies the type of transaction that is to be created. | 
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

[**ResponseTransactionType**](ResponseTransactionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

