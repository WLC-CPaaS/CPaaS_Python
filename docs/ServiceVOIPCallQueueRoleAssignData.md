# ServiceVOIPCallQueueRoleAssignData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**recipients** | **List[Dict[str, List[str]]]** |  | 
**set_membership** | **bool** |  | 

## Example

```python
from openapi_client.models.service_voip_call_queue_role_assign_data import ServiceVOIPCallQueueRoleAssignData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPCallQueueRoleAssignData from a JSON string
service_voip_call_queue_role_assign_data_instance = ServiceVOIPCallQueueRoleAssignData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPCallQueueRoleAssignData.to_json())

# convert the object into a dict
service_voip_call_queue_role_assign_data_dict = service_voip_call_queue_role_assign_data_instance.to_dict()
# create an instance of ServiceVOIPCallQueueRoleAssignData from a dict
service_voip_call_queue_role_assign_data_from_dict = ServiceVOIPCallQueueRoleAssignData.from_dict(service_voip_call_queue_role_assign_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


