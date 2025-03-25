# ServiceChannelOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answered** | **bool** |  | [optional] 
**authorizing_id** | **str** |  | [optional] 
**authorizing_type** | **str** |  | [optional] 
**callflow_id** | **str** |  | [optional] 
**channel_authorized** | **bool** |  | [optional] 
**custom_application_vars** | **Dict[str, object]** |  | [optional] 
**custom_auth_headers** | **Dict[str, object]** |  | [optional] 
**custom_channel_vars** | **Dict[str, object]** |  | [optional] 
**custom_sip_headers** | **Dict[str, object]** |  | [optional] 
**destination** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**elapsed_s** | **int** |  | [optional] 
**from_tag** | **str** |  | [optional] 
**interaction_id** | **str** |  | [optional] 
**is_loopback** | **bool** |  | [optional] 
**is_onhold** | **bool** |  | [optional] 
**other_leg** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**presence_id** | **str** |  | [optional] 
**request** | **str** |  | [optional] 
**reseller_id** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**to_tag** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_channel_output import ServiceChannelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChannelOutput from a JSON string
service_channel_output_instance = ServiceChannelOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceChannelOutput.to_json())

# convert the object into a dict
service_channel_output_dict = service_channel_output_instance.to_dict()
# create an instance of ServiceChannelOutput from a dict
service_channel_output_from_dict = ServiceChannelOutput.from_dict(service_channel_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


