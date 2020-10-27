# swagger_client.AccountsApi

All URIs are relative to *https://sandbox.mobilemoneyapi.io/simulator/v1.1/passthrough/mm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_accountname_get**](AccountsApi.md#accounts_account_id_accountname_get) | **GET** /accounts/{accountId}/accountname | View Account Name
[**accounts_account_id_balance_get**](AccountsApi.md#accounts_account_id_balance_get) | **GET** /accounts/{accountId}/balance | View Account Balance
[**accounts_account_id_statemententries_get**](AccountsApi.md#accounts_account_id_statemententries_get) | **GET** /accounts/{accountId}/statemententries | View Account Statements
[**accounts_account_id_status_get**](AccountsApi.md#accounts_account_id_status_get) | **GET** /accounts/{accountId}/status | View Account Status
[**accounts_account_id_transactions_get**](AccountsApi.md#accounts_account_id_transactions_get) | **GET** /accounts/{accountId}/transactions | View Account Specific Transaction
[**accounts_balance_get**](AccountsApi.md#accounts_balance_get) | **GET** /accounts/balance | View Account Balance
[**accounts_identifier_type_identifier_accountname_get**](AccountsApi.md#accounts_identifier_type_identifier_accountname_get) | **GET** /accounts/{identifierType}/{identifier}/accountname | View Account Name
[**accounts_identifier_type_identifier_balance_get**](AccountsApi.md#accounts_identifier_type_identifier_balance_get) | **GET** /accounts/{identifierType}/{identifier}/balance | View Account Balance
[**accounts_identifier_type_identifier_statemententries_get**](AccountsApi.md#accounts_identifier_type_identifier_statemententries_get) | **GET** /accounts/{identifierType}/{identifier}/statemententries | View Account Statements
[**accounts_identifier_type_identifier_status_get**](AccountsApi.md#accounts_identifier_type_identifier_status_get) | **GET** /accounts/{identifierType}/{identifier}/status | View Account Status
[**accounts_identifier_type_identifier_transactions_get**](AccountsApi.md#accounts_identifier_type_identifier_transactions_get) | **GET** /accounts/{identifierType}/{identifier}/transactions | View Account Specific Transaction
[**statemententries_transaction_reference_get**](AccountsApi.md#statemententries_transaction_reference_get) | **GET** /statemententries/{transactionReference} | View Specific Statement

# **accounts_account_id_accountname_get**
> ResponseAccountName accounts_account_id_accountname_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Name

This endpoint returns the status of a given account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
    # View Account Name
    api_response = api_instance.accounts_account_id_accountname_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_account_id_accountname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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

[**ResponseAccountName**](ResponseAccountName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_balance_get**
> ResponseAccountBalance accounts_account_id_balance_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Balance

This endpoint returns the balance of an account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
    # View Account Balance
    api_response = api_instance.accounts_account_id_balance_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_account_id_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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

[**ResponseAccountBalance**](ResponseAccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_statemententries_get**
> list[ResponseStatementEntries] accounts_account_id_statemententries_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, display_type=display_type)

View Account Statements

The Statement Entries API enables generic representations of transactions to be returned. Typically, the returned representations are used for the purposes of presenting a statement to the account holder. In order to return a statement, an account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
transaction_status = 'transaction_status_example' # str | Query variable to uniquely identify the transaction status. (optional)
display_type = 'display_type_example' # str | Query parameter to to identify the display type of the statement entries to be returned. (optional)

try:
    # View Account Statements
    api_response = api_instance.accounts_account_id_statemententries_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, display_type=display_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_account_id_statemententries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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
 **transaction_status** | **str**| Query variable to uniquely identify the transaction status. | [optional] 
 **display_type** | **str**| Query parameter to to identify the display type of the statement entries to be returned. | [optional] 

### Return type

[**list[ResponseStatementEntries]**](ResponseStatementEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_status_get**
> ResponseAccountStatus accounts_account_id_status_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Status

This endpoint returns the current status of an account. This API accepts multiple identifiers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
    # View Account Status
    api_response = api_instance.accounts_account_id_status_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_account_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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

[**ResponseAccountStatus**](ResponseAccountStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_transactions_get**
> list[ResponseTransaction] accounts_account_id_transactions_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, transaction_type=transaction_type)

View Account Specific Transaction

This endpoint returns transactions linked to a specific account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 'account_id_example' # str | Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference.
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
transaction_status = 'transaction_status_example' # str | Query variable to uniquely identify the transaction status. (optional)
transaction_type = 'transaction_type_example' # str | Identifies the type of transaction. (optional)

try:
    # View Account Specific Transaction
    api_response = api_instance.accounts_account_id_transactions_get(account_id, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, transaction_type=transaction_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_account_id_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Path variable to uniquely identify an account. Up to three account identifiers can be supplied. Identifiers are delimited by $ and values are delimited by @. Example: organisationid@1234$accountid@3333. Valid account identifiers are accountcategory, bankaccountno, accountrank, identityalias, iban, accountid, msisdn, swiftbic, sortcode, organisationid, username, walletid, linkref, consumerno, serviceprovider, storeid, bankname, bankaccounttitle, emailaddress, mandatereference. | 
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
 **transaction_status** | **str**| Query variable to uniquely identify the transaction status. | [optional] 
 **transaction_type** | **str**| Identifies the type of transaction. | [optional] 

### Return type

[**list[ResponseTransaction]**](ResponseTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_balance_get**
> ResponseAccountBalance accounts_balance_get(x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Balance

This endpoint returns the balance of an account. As the account is not passed as a parameter, the account is assumed to be that of the calling client.\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
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
    # View Account Balance
    api_response = api_instance.accounts_balance_get(x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[**ResponseAccountBalance**](ResponseAccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_accountname_get**
> ResponseAccountName accounts_identifier_type_identifier_accountname_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Name

This endpoint returns the name of an account holder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
    # View Account Name
    api_response = api_instance.accounts_identifier_type_identifier_accountname_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_identifier_type_identifier_accountname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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

[**ResponseAccountName**](ResponseAccountName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_balance_get**
> ResponseAccountBalance accounts_identifier_type_identifier_balance_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Balance

This endpoint returns the balance of an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
    # View Account Balance
    api_response = api_instance.accounts_identifier_type_identifier_balance_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_identifier_type_identifier_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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

[**ResponseAccountBalance**](ResponseAccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_statemententries_get**
> list[ResponseStatementEntries] accounts_identifier_type_identifier_statemententries_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, display_type=display_type)

View Account Statements

The Statement Entries API enables generic representations of transactions to be returned. Typically, the returned representations are used for the purposes of presenting a statement to the account holder. In order to return a statement, an account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
transaction_status = 'transaction_status_example' # str | Query variable to uniquely identify the transaction status. (optional)
display_type = 'display_type_example' # str | Query parameter to to identify the display type of the statement entries to be returned. (optional)

try:
    # View Account Statements
    api_response = api_instance.accounts_identifier_type_identifier_statemententries_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, display_type=display_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_identifier_type_identifier_statemententries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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
 **transaction_status** | **str**| Query variable to uniquely identify the transaction status. | [optional] 
 **display_type** | **str**| Query parameter to to identify the display type of the statement entries to be returned. | [optional] 

### Return type

[**list[ResponseStatementEntries]**](ResponseStatementEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_status_get**
> ResponseAccountStatus accounts_identifier_type_identifier_status_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Account Status

This endpoint returns the current status of an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
    # View Account Status
    api_response = api_instance.accounts_identifier_type_identifier_status_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_identifier_type_identifier_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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

[**ResponseAccountStatus**](ResponseAccountStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_identifier_type_identifier_transactions_get**
> list[ResponseTransaction] accounts_identifier_type_identifier_transactions_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, transaction_type=transaction_type)

View Account Specific Transaction

This endpoint returns transactions linked to a specific account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
identifier_type = 'identifier_type_example' # str | Path variable to specify the type of the identifier that is used to identify the account.
identifier = 'identifier_example' # str | Path variable that contains the account identifier.
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
transaction_status = 'transaction_status_example' # str | Query variable to uniquely identify the transaction status. (optional)
transaction_type = 'transaction_type_example' # str | Identifies the type of transaction. (optional)

try:
    # View Account Specific Transaction
    api_response = api_instance.accounts_identifier_type_identifier_transactions_get(identifier_type, identifier, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier, limit=limit, offset=offset, from_date_time=from_date_time, to_date_time=to_date_time, transaction_status=transaction_status, transaction_type=transaction_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_identifier_type_identifier_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Path variable to specify the type of the identifier that is used to identify the account. | 
 **identifier** | **str**| Path variable that contains the account identifier. | 
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
 **transaction_status** | **str**| Query variable to uniquely identify the transaction status. | [optional] 
 **transaction_type** | **str**| Identifies the type of transaction. | [optional] 

### Return type

[**list[ResponseTransaction]**](ResponseTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statemententries_transaction_reference_get**
> ResponseStatementEntries statemententries_transaction_reference_get(transaction_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)

View Specific Statement

The Statement Entries API enables generic representations of transactions to be returned. Typically, the returned representations are used for the purposes of presenting a statement to the account holder. In order to return a statement, a transaction reference must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
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
    # View Specific Statement
    api_response = api_instance.statemententries_transaction_reference_get(transaction_reference, x_date=x_date, x_api_key=x_api_key, x_user_bearer=x_user_bearer, x_client_id=x_client_id, x_content_hash=x_content_hash, x_user_credential_1=x_user_credential_1, x_user_credential_2=x_user_credential_2, x_channel=x_channel, x_account_holding_institution_identifier_type=x_account_holding_institution_identifier_type, x_account_holding_institution_identifier=x_account_holding_institution_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->statemententries_transaction_reference_get: %s\n" % e)
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

[**ResponseStatementEntries**](ResponseStatementEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

