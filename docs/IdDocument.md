# IdDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type** | **str** | Indicates the type of identification for the KYC subject, e.g. passport, driving licence etc. | 
**id_number** | **str** | Reference pertaining to the type of identification for the KYC subject. | [optional] 
**issue_date** | **date** | Date of issue for the identification document. | [optional] 
**expiry_date** | **date** | Date of expiry for the identification document. | [optional] 
**issuer** | **str** | Indicates the organisation/government entity that issued the ID document. | [optional] 
**issuer_place** | **str** | Place of issue for the identification type. | [optional] 
**issuer_country** | [**Object**](Object.md) | Country where the identification type was issued. | [optional] 
**other_iddescription** | **str** | Where an ID Type of otherid is specified, a description of the type of identification can be provided in this property. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

