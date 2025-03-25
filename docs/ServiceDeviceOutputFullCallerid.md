# ServiceDeviceOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ServiceDeviceOutputFullCalleridEmergency**](ServiceDeviceOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ServiceDeviceOutputFullCalleridExternal**](ServiceDeviceOutputFullCalleridExternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_device_output_full_callerid import ServiceDeviceOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeviceOutputFullCallerid from a JSON string
service_device_output_full_callerid_instance = ServiceDeviceOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ServiceDeviceOutputFullCallerid.to_json())

# convert the object into a dict
service_device_output_full_callerid_dict = service_device_output_full_callerid_instance.to_dict()
# create an instance of ServiceDeviceOutputFullCallerid from a dict
service_device_output_full_callerid_from_dict = ServiceDeviceOutputFullCallerid.from_dict(service_device_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


