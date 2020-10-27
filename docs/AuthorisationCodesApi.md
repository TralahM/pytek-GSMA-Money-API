# swagger_client.AuthorisationCodesApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_authorisation_code_authorisation_code_get**](AuthorisationCodesApi.md#accounts_account_id_authorisation_code_authorisation_code_get) | **GET** /accounts/{accountId}/authorisationcodes/{authorisationCode} | View an Authorisation Code
[**accounts_account_id_authorisation_codes_authorisation_code_patch**](AuthorisationCodesApi.md#accounts_account_id_authorisation_codes_authorisation_code_patch) | **PATCH** /accounts/{accountId}/authorisationcodes/{authorisationCode} | Update an Authorisation Code
[**accounts_account_id_authorisationcodes_post**](AuthorisationCodesApi.md#accounts_account_id_authorisationcodes_post) | **POST** /accounts/{accountId}/authorisationcodes | Create an Authorisation Code
[**accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get**](AuthorisationCodesApi.md#accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get) | **GET** /accounts/{identifierType}/{identifier}/authorisationcodes/{authorisationCode} | View an Authorisation Code
[**accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch**](AuthorisationCodesApi.md#accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch) | **PATCH** /accounts/{identifierType}/{identifier}/authorisationcodes/{authorisationCode} | Cancel an Authorisation Code
[**accounts_identifier_type_identifier_authorisation_codes_post**](AuthorisationCodesApi.md#accounts_identifier_type_identifier_authorisation_codes_post) | **POST** /accounts/{identifierType}/{identifier}/authorisationcodes | Create an Authorisation Code via an account identifier.

# **accounts_account_id_authorisation_code_authorisation_code_get**
> ResponseAuthorisationCode accounts_account_id_authorisation_code_authorisation_code_get(account_id, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View an Authorisation Code

This endpoint returns a specific Authorisation Code linked to an account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
authorisation_code = 'authorisation_code_example' # str | Path variable to uniquely identify an authorisation code.
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
    # View an Authorisation Code
    api_response = api_instance.accounts_account_id_authorisation_code_authorisation_code_get(account_id, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_account_id_authorisation_code_authorisation_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
 **authorisation_code** | **str**| Path variable to uniquely identify an authorisation code. | 
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

[**ResponseAuthorisationCode**](ResponseAuthorisationCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_authorisation_codes_authorisation_code_patch**
> RequestStateObject accounts_account_id_authorisation_codes_authorisation_code_patch(body, account_id, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)

Update an Authorisation Code

This endpoint updates a specific Authorisation Code linked to an account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
authorisation_code = 'authorisation_code_example' # str | Path variable to uniquely identify an authorisation code.
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
    # Update an Authorisation Code
    api_response = api_instance.accounts_account_id_authorisation_codes_authorisation_code_patch(body, account_id, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_account_id_authorisation_codes_authorisation_code_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
 **authorisation_code** | **str**| Path variable to uniquely identify an authorisation code. | 
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

# **accounts_account_id_authorisationcodes_post**
> ResponseAuthorisationCode accounts_account_id_authorisationcodes_post(body, account_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create an Authorisation Code

this endpoint allows allows a mobile money payer or payee to generate a code which when presented to the other party, can be redeemed for an amount set by the payer or payee, depending upon the use case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
body = swagger_client.RequestAuthorisationCode() # RequestAuthorisationCode | Represents the request body of an Authorisation Code.
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
    # Create an Authorisation Code
    api_response = api_instance.accounts_account_id_authorisationcodes_post(body, account_id, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_account_id_authorisationcodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestAuthorisationCode**](RequestAuthorisationCode.md)| Represents the request body of an Authorisation Code. | 
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

[**ResponseAuthorisationCode**](ResponseAuthorisationCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get**
> ResponseAuthorisationCode accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get(identifier_type, identifier, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View an Authorisation Code

This endpoint returns a specific Authorisation Code linked to an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
authorisation_code = 'authorisation_code_example' # str | Path variable to uniquely identify an authorisation code.
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
    # View an Authorisation Code
    api_response = api_instance.accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get(identifier_type, identifier, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_identifier_type_identifier_authorisation_codes_authorisation_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
 **authorisation_code** | **str**| Path variable to uniquely identify an authorisation code. | 
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

[**ResponseAuthorisationCode**](ResponseAuthorisationCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch**
> RequestStateObject accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch(body, identifier_type, identifier, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)

Cancel an Authorisation Code

This endpoint cancels a specific authorisation code linked to an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
body = [swagger_client.RequestGenericPatch()] # list[RequestGenericPatch] | Represents the request body of a batch of generic Patch operation.
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
authorisation_code = 'authorisation_code_example' # str | Path variable to uniquely identify an authorisation code.
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
    # Cancel an Authorisation Code
    api_response = api_instance.accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch(body, identifier_type, identifier, authorisation_code, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_identifier_type_identifier_authorisation_codes_authorisation_code_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RequestGenericPatch]**](RequestGenericPatch.md)| Represents the request body of a batch of generic Patch operation. | 
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
 **authorisation_code** | **str**| Path variable to uniquely identify an authorisation code. | 
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

# **accounts_identifier_type_identifier_authorisation_codes_post**
> ResponseAuthorisationCode accounts_identifier_type_identifier_authorisation_codes_post(body, identifier_type, identifier, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

Create an Authorisation Code via an account identifier.

This endpoint allows allows a mobile money payer or payee to generate a code which when presented to the other party, can be redeemed for an amount set by the payer or payee, depending upon the use case.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorisationCodesApi()
body = swagger_client.RequestAuthorisationCode() # RequestAuthorisationCode | Represents the request body of an Authorisation Code.
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
    # Create an Authorisation Code via an account identifier.
    api_response = api_instance.accounts_identifier_type_identifier_authorisation_codes_post(body, identifier_type, identifier, x_date=x_date, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_callback_url=x_callback_url, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorisationCodesApi->accounts_identifier_type_identifier_authorisation_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestAuthorisationCode**](RequestAuthorisationCode.md)| Represents the request body of an Authorisation Code. | 
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

[**ResponseAuthorisationCode**](ResponseAuthorisationCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

