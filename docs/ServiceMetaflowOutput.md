# ServiceMetaflowOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_digit** | **str** |  | [optional] 
**numbers** | [**Dict[str, ServiceMetaflowPattern]**](ServiceMetaflowPattern.md) |  | [optional] 
**patterns** | [**Dict[str, ServiceMetaflowPattern]**](ServiceMetaflowPattern.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_metaflow_output import ServiceMetaflowOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetaflowOutput from a JSON string
service_metaflow_output_instance = ServiceMetaflowOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceMetaflowOutput.to_json())

# convert the object into a dict
service_metaflow_output_dict = service_metaflow_output_instance.to_dict()
# create an instance of ServiceMetaflowOutput from a dict
service_metaflow_output_from_dict = ServiceMetaflowOutput.from_dict(service_metaflow_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


