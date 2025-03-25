# ServiceCallQueueRolesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_call_queue_roles_output import ServiceCallQueueRolesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallQueueRolesOutput from a JSON string
service_call_queue_roles_output_instance = ServiceCallQueueRolesOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceCallQueueRolesOutput.to_json())

# convert the object into a dict
service_call_queue_roles_output_dict = service_call_queue_roles_output_instance.to_dict()
# create an instance of ServiceCallQueueRolesOutput from a dict
service_call_queue_roles_output_from_dict = ServiceCallQueueRolesOutput.from_dict(service_call_queue_roles_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


