# ServiceGroupOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**Dict[str, ServiceEndpoint]**](ServiceEndpoint.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_group_output_full import ServiceGroupOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroupOutputFull from a JSON string
service_group_output_full_instance = ServiceGroupOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceGroupOutputFull.to_json())

# convert the object into a dict
service_group_output_full_dict = service_group_output_full_instance.to_dict()
# create an instance of ServiceGroupOutputFull from a dict
service_group_output_full_from_dict = ServiceGroupOutputFull.from_dict(service_group_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


