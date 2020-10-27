# ResponseAccountBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_balance** | [**Object**](Object.md) | Current outstanding balance on the account. | [optional] 
**available_balance** | [**Object**](Object.md) | Indicates the balance that is able to be debited for an account. This balance is only provided on some API provider systems. | [optional] 
**reserved_balance** | [**Object**](Object.md) | Indicates the portion of the balance that is reserved, i.e. intended to be debited. This balance is only provided on some API provider systems.\&quot; | [optional] 
**uncleared_balance** | [**Object**](Object.md) | Indicates the sum of uncleared funds in an account, i.e. the funds that are awaiting a credit confirmation. | [optional] 
**currency** | [**Object**](Object.md) | Currency for all returned balances. | [optional] 
**account_status** | [**AccountStatus**](AccountStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

