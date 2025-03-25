# ServiceGroupOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | **int** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**group_endpoints** | [**Dict[str, ServiceEndpoint]**](ServiceEndpoint.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_group_output_short import ServiceGroupOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroupOutputShort from a JSON string
service_group_output_short_instance = ServiceGroupOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceGroupOutputShort.to_json())

# convert the object into a dict
service_group_output_short_dict = service_group_output_short_instance.to_dict()
# create an instance of ServiceGroupOutputShort from a dict
service_group_output_short_from_dict = ServiceGroupOutputShort.from_dict(service_group_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


