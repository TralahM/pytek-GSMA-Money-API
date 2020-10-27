# swagger_client.LinksApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_links_link_reference_get**](LinksApi.md#accounts_account_id_links_link_reference_get) | **GET** /accounts/{accountId}/links/{linkReference} | View A Link
[**accounts_account_id_links_link_reference_patch**](LinksApi.md#accounts_account_id_links_link_reference_patch) | **PATCH** /accounts/{accountId}/links/{linkReference} | Update A Link
[**accounts_account_id_links_post**](LinksApi.md#accounts_account_id_links_post) | **POST** /accounts/{accountId}/links | Create A Link
[**accounts_identifier_type_identifier_links_link_reference_get**](LinksApi.md#accounts_identifier_type_identifier_links_link_reference_get) | **GET** /accounts/{identifierType}/{identifier}/links/{linkReference} | View A Link
[**accounts_identifier_type_identifier_links_link_reference_patch**](LinksApi.md#accounts_identifier_type_identifier_links_link_reference_patch) | **PATCH** /accounts/{identifierType}/{identifier}/links/{linkReference} | Update A Link
[**accounts_identifier_type_identifier_links_post**](LinksApi.md#accounts_identifier_type_identifier_links_post) | **POST** /accounts/{identifierType}/{identifier}/links | Create A Link

# **accounts_account_id_links_link_reference_get**
> ResponseLink accounts_account_id_links_link_reference_get(account_id, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View A Link

This endpoint returns a specific link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
link_reference = 'link_reference_example' # str | Path variable to uniquely identify a link.
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
    # View A Link
    api_response = api_instance.accounts_account_id_links_link_reference_get(account_id, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_account_id_links_link_reference_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
 **link_reference** | **str**| Path variable to uniquely identify a link. | 
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

[**ResponseLink**](ResponseLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_links_link_reference_patch**
> RequestStateObject accounts_account_id_links_link_reference_patch(body, account_id, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)

Update A Link

This endpoint updates a specific link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
link_reference = 'link_reference_example' # str | Path variable to uniquely identify a link.
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
    # Update A Link
    api_response = api_instance.accounts_account_id_links_link_reference_patch(body, account_id, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_account_id_links_link_reference_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
 **link_reference** | **str**| Path variable to uniquely identify a link. | 
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

# **accounts_account_id_links_post**
> ResponseLink accounts_account_id_links_post(body, account_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create A Link

Provided with a valid object representation, this endpoint allows a new link to be created for a specific account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
body = swagger_client.RequestLink() # RequestLink | Represents the request body of a Link."
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
    # Create A Link
    api_response = api_instance.accounts_account_id_links_post(body, account_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_account_id_links_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestLink**](RequestLink.md)| Represents the request body of a Link.&quot; | 
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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

[**ResponseLink**](ResponseLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_links_link_reference_get**
> ResponseLink accounts_identifier_type_identifier_links_link_reference_get(identifier_type, identifier, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View A Link

This endpoint returns a specific link for a given account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
link_reference = 'link_reference_example' # str | Path variable to uniquely identify a link.
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
    # View A Link
    api_response = api_instance.accounts_identifier_type_identifier_links_link_reference_get(identifier_type, identifier, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_identifier_type_identifier_links_link_reference_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
 **link_reference** | **str**| Path variable to uniquely identify a link. | 
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

[**ResponseLink**](ResponseLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_links_link_reference_patch**
> RequestStateObject accounts_identifier_type_identifier_links_link_reference_patch(body, identifier_type, identifier, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)

Update A Link

This endpoint updates a specific link.\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
link_reference = 'link_reference_example' # str | Path variable to uniquely identify a link.
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
    # Update A Link
    api_response = api_instance.accounts_identifier_type_identifier_links_link_reference_patch(body, identifier_type, identifier, link_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_identifier_type_identifier_links_link_reference_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
 **link_reference** | **str**| Path variable to uniquely identify a link. | 
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

# **accounts_identifier_type_identifier_links_post**
> ResponseLink accounts_identifier_type_identifier_links_post(body, identifier_type, identifier, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create A Link

Provided with a valid object representation, this endpoint allows a new link to be created for a specific account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinksApi()
body = swagger_client.RequestLink() # RequestLink | Represents the request body of a Link."
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
    # Create A Link
    api_response = api_instance.accounts_identifier_type_identifier_links_post(body, identifier_type, identifier, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->accounts_identifier_type_identifier_links_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestLink**](RequestLink.md)| Represents the request body of a Link.&quot; | 
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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

[**ResponseLink**](ResponseLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

