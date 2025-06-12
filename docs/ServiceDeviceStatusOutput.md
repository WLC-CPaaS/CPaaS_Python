# ServiceDeviceStatusOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**registered** | **bool** |  | [optional] 
**registrable** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.service_device_status_output import ServiceDeviceStatusOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeviceStatusOutput from a JSON string
service_device_status_output_instance = ServiceDeviceStatusOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDeviceStatusOutput.to_json())

# convert the object into a dict
service_device_status_output_dict = service_device_status_output_instance.to_dict()
# create an instance of ServiceDeviceStatusOutput from a dict
service_device_status_output_from_dict = ServiceDeviceStatusOutput.from_dict(service_device_status_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


