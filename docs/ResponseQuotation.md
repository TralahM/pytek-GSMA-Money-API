# ResponseQuotation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_date** | [**RequestDate**](RequestDate.md) |  | 
**debit_party** | [**DebitPartyArray**](DebitPartyArray.md) |  | 
**credit_party** | [**CreditPartyArray**](CreditPartyArray.md) |  | 
**sender_kyc** | [**Kyc**](Kyc.md) |  | [optional] 
**recipient_kyc** | [**Kyc**](Kyc.md) |  | [optional] 
**request_amount** | [**Object**](Object.md) | The requested quotation amount. | 
**request_currency** | [**Object**](Object.md) | Currency of the requested quotation amount | 
**type** | [**Type**](Type.md) |  | [optional] 
**sub_type** | [**SubType**](SubType.md) |  | [optional] 
**chosen_delivery_method** | [**Object**](Object.md) | The delivery method chosen by the sending end user as the specific delivery method to be used in the quotes received. | [optional] 
**quotes** | [**QuoteArray**](QuoteArray.md) |  | [optional] 
**sender_blocking_reason** | [**SenderBlockingReason**](SenderBlockingReason.md) |  | [optional] 
**recipient_blocking_reason** | [**RecipientBlockingReason**](RecipientBlockingReason.md) |  | [optional] 
**metadata** | [**MetadataArray**](MetadataArray.md) |  | [optional] 
**quotation_reference** | [**QuotationReference**](QuotationReference.md) |  | 
**quotation_status** | [**QuotationStatus**](QuotationStatus.md) |  | [optional] 
**creation_date** | [**CreationDate**](CreationDate.md) |  | [optional] 
**modification_date** | [**ModificationDate**](ModificationDate.md) |  | [optional] 
**date_created** | [**DateCreated**](DateCreated.md) |  | [optional] 
**date_modified** | [**DateModified**](DateModified.md) |  | [optional] 
**available_delivery_method** | [**Object**](Object.md) | Delivery Method that is possible for the intended recipient. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

