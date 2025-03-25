# ServiceVOIPDeviceAddEdit3a


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_format** | **str** |  | 
**password** | **str** |  | [optional] 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.service_voip_device_add_edit3a import ServiceVOIPDeviceAddEdit3a

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPDeviceAddEdit3a from a JSON string
service_voip_device_add_edit3a_instance = ServiceVOIPDeviceAddEdit3a.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPDeviceAddEdit3a.to_json())

# convert the object into a dict
service_voip_device_add_edit3a_dict = service_voip_device_add_edit3a_instance.to_dict()
# create an instance of ServiceVOIPDeviceAddEdit3a from a dict
service_voip_device_add_edit3a_from_dict = ServiceVOIPDeviceAddEdit3a.from_dict(service_voip_device_add_edit3a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


