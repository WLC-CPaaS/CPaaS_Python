# ModelsDeviceOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ModelsDeviceOutputFullCalleridEmergency**](ModelsDeviceOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ModelsDeviceOutputFullCalleridExternal**](ModelsDeviceOutputFullCalleridExternal.md) |  | [optional] 
**internal** | [**ModelsDeviceOutputFullCalleridInternal**](ModelsDeviceOutputFullCalleridInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_device_output_full_callerid import ModelsDeviceOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsDeviceOutputFullCallerid from a JSON string
models_device_output_full_callerid_instance = ModelsDeviceOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ModelsDeviceOutputFullCallerid.to_json())

# convert the object into a dict
models_device_output_full_callerid_dict = models_device_output_full_callerid_instance.to_dict()
# create an instance of ModelsDeviceOutputFullCallerid from a dict
models_device_output_full_callerid_from_dict = ModelsDeviceOutputFullCallerid.from_dict(models_device_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


