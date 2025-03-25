# ServiceCallForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_call_forward import ServiceCallForward

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallForward from a JSON string
service_call_forward_instance = ServiceCallForward.from_json(json)
# print the JSON string representation of the object
print(ServiceCallForward.to_json())

# convert the object into a dict
service_call_forward_dict = service_call_forward_instance.to_dict()
# create an instance of ServiceCallForward from a dict
service_call_forward_from_dict = ServiceCallForward.from_dict(service_call_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


