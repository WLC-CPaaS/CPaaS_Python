# ServiceCallflowOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**modules** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**numbers** | **List[str]** |  | [optional] 
**patterns** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_callflow_output_short import ServiceCallflowOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallflowOutputShort from a JSON string
service_callflow_output_short_instance = ServiceCallflowOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceCallflowOutputShort.to_json())

# convert the object into a dict
service_callflow_output_short_dict = service_callflow_output_short_instance.to_dict()
# create an instance of ServiceCallflowOutputShort from a dict
service_callflow_output_short_from_dict = ServiceCallflowOutputShort.from_dict(service_callflow_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


