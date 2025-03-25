# ServiceChannelRunMetaflowData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**Dict[str, ServiceChannelRunMetaflowData]**](ServiceChannelRunMetaflowData.md) |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**module** | **str** |  | 

## Example

```python
from openapi_client.models.service_channel_run_metaflow_data import ServiceChannelRunMetaflowData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChannelRunMetaflowData from a JSON string
service_channel_run_metaflow_data_instance = ServiceChannelRunMetaflowData.from_json(json)
# print the JSON string representation of the object
print(ServiceChannelRunMetaflowData.to_json())

# convert the object into a dict
service_channel_run_metaflow_data_dict = service_channel_run_metaflow_data_instance.to_dict()
# create an instance of ServiceChannelRunMetaflowData from a dict
service_channel_run_metaflow_data_from_dict = ServiceChannelRunMetaflowData.from_dict(service_channel_run_metaflow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


