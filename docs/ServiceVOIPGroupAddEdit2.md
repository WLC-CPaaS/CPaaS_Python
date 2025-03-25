# ServiceVOIPGroupAddEdit2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**Dict[str, ServiceEndpoint]**](ServiceEndpoint.md) |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.service_voip_group_add_edit2 import ServiceVOIPGroupAddEdit2

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPGroupAddEdit2 from a JSON string
service_voip_group_add_edit2_instance = ServiceVOIPGroupAddEdit2.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPGroupAddEdit2.to_json())

# convert the object into a dict
service_voip_group_add_edit2_dict = service_voip_group_add_edit2_instance.to_dict()
# create an instance of ServiceVOIPGroupAddEdit2 from a dict
service_voip_group_add_edit2_from_dict = ServiceVOIPGroupAddEdit2.from_dict(service_voip_group_add_edit2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


