# ServiceMetaflowPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**Dict[str, ServiceMetaflowPattern]**](ServiceMetaflowPattern.md) |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**module** | **str** |  | 

## Example

```python
from openapi_client.models.service_metaflow_pattern import ServiceMetaflowPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetaflowPattern from a JSON string
service_metaflow_pattern_instance = ServiceMetaflowPattern.from_json(json)
# print the JSON string representation of the object
print(ServiceMetaflowPattern.to_json())

# convert the object into a dict
service_metaflow_pattern_dict = service_metaflow_pattern_instance.to_dict()
# create an instance of ServiceMetaflowPattern from a dict
service_metaflow_pattern_from_dict = ServiceMetaflowPattern.from_dict(service_metaflow_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


