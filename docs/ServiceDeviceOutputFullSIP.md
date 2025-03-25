# ServiceDeviceOutputFullSIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_format** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_device_output_full_sip import ServiceDeviceOutputFullSIP

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeviceOutputFullSIP from a JSON string
service_device_output_full_sip_instance = ServiceDeviceOutputFullSIP.from_json(json)
# print the JSON string representation of the object
print(ServiceDeviceOutputFullSIP.to_json())

# convert the object into a dict
service_device_output_full_sip_dict = service_device_output_full_sip_instance.to_dict()
# create an instance of ServiceDeviceOutputFullSIP from a dict
service_device_output_full_sip_from_dict = ServiceDeviceOutputFullSIP.from_dict(service_device_output_full_sip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


