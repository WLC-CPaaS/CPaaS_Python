# ServiceVOIPDeviceAddEditProvision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_brand** | **str** |  | [optional] 
**endpoint_family** | **str** |  | [optional] 
**endpoint_model** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_device_add_edit_provision import ServiceVOIPDeviceAddEditProvision

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPDeviceAddEditProvision from a JSON string
service_voip_device_add_edit_provision_instance = ServiceVOIPDeviceAddEditProvision.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPDeviceAddEditProvision.to_json())

# convert the object into a dict
service_voip_device_add_edit_provision_dict = service_voip_device_add_edit_provision_instance.to_dict()
# create an instance of ServiceVOIPDeviceAddEditProvision from a dict
service_voip_device_add_edit_provision_from_dict = ServiceVOIPDeviceAddEditProvision.from_dict(service_voip_device_add_edit_provision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


