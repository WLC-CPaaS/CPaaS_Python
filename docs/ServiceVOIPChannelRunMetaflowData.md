# ServiceVOIPChannelRunMetaflowData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**Dict[str, ServiceVOIPChannelRunMetaflowData]**](ServiceVOIPChannelRunMetaflowData.md) |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**module** | **str** |  | 

## Example

```python
from openapi_client.models.service_voip_channel_run_metaflow_data import ServiceVOIPChannelRunMetaflowData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPChannelRunMetaflowData from a JSON string
service_voip_channel_run_metaflow_data_instance = ServiceVOIPChannelRunMetaflowData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPChannelRunMetaflowData.to_json())

# convert the object into a dict
service_voip_channel_run_metaflow_data_dict = service_voip_channel_run_metaflow_data_instance.to_dict()
# create an instance of ServiceVOIPChannelRunMetaflowData from a dict
service_voip_channel_run_metaflow_data_from_dict = ServiceVOIPChannelRunMetaflowData.from_dict(service_voip_channel_run_metaflow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


