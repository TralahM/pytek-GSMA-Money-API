# RequestStateObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_correlation_id** | **str** | A unique identifier issued by the provider to enable the client to identify the RequestState resource on subsequent polling requests. Must be supplied as a UUID. | 
**status** | **str** | Indicates the status of the request. | 
**pending_reason** | **str** | A textual description that can be provided to describe the reason for a pending status. | [optional] 
**notification_method** | **str** | Indicates whether a callback will be issued or whether the client will need to poll. | 
**object_reference** | **str** | Provides a reference to the subject resource, e.g. transaction reference. | [optional] 
**expiry_time** | **datetime** | Indicate the time by which the provider will fail the request if completion criteria have not been met. For an example, a debit party failing to authorise within the allowed period. | [optional] 
**poll_limit** | [**BigDecimal**](BigDecimal.md) | Indicates the number of poll attempts for the given requeststate resource that will be allowed by the provider. | [optional] 
**error** | [**Object**](Object.md) | If the asynchronous processing failed, details of the error will be returned here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

