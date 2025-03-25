# ServiceChannelRunActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**moh** | **str** |  | [optional] 
**takeback_dtmf** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_channel_run_action_data import ServiceChannelRunActionData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChannelRunActionData from a JSON string
service_channel_run_action_data_instance = ServiceChannelRunActionData.from_json(json)
# print the JSON string representation of the object
print(ServiceChannelRunActionData.to_json())

# convert the object into a dict
service_channel_run_action_data_dict = service_channel_run_action_data_instance.to_dict()
# create an instance of ServiceChannelRunActionData from a dict
service_channel_run_action_data_from_dict = ServiceChannelRunActionData.from_dict(service_channel_run_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


