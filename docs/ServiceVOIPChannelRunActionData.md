# ServiceVOIPChannelRunActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**moh** | **str** |  | [optional] 
**takeback_dtmf** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_channel_run_action_data import ServiceVOIPChannelRunActionData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPChannelRunActionData from a JSON string
service_voip_channel_run_action_data_instance = ServiceVOIPChannelRunActionData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPChannelRunActionData.to_json())

# convert the object into a dict
service_voip_channel_run_action_data_dict = service_voip_channel_run_action_data_instance.to_dict()
# create an instance of ServiceVOIPChannelRunActionData from a dict
service_voip_channel_run_action_data_from_dict = ServiceVOIPChannelRunActionData.from_dict(service_voip_channel_run_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


