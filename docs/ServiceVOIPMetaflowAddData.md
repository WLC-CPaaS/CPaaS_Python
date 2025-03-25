# ServiceVOIPMetaflowAddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_digit** | **str** |  | [optional] 
**numbers** | [**Dict[str, ServiceMetaflowPattern]**](ServiceMetaflowPattern.md) |  | [optional] 
**patterns** | [**Dict[str, ServiceMetaflowPattern]**](ServiceMetaflowPattern.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_metaflow_add_data import ServiceVOIPMetaflowAddData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPMetaflowAddData from a JSON string
service_voip_metaflow_add_data_instance = ServiceVOIPMetaflowAddData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPMetaflowAddData.to_json())

# convert the object into a dict
service_voip_metaflow_add_data_dict = service_voip_metaflow_add_data_instance.to_dict()
# create an instance of ServiceVOIPMetaflowAddData from a dict
service_voip_metaflow_add_data_from_dict = ServiceVOIPMetaflowAddData.from_dict(service_voip_metaflow_add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


