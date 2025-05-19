# ServiceDocsDeviceReboot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_device_reboot import ServiceDocsDeviceReboot

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsDeviceReboot from a JSON string
service_docs_device_reboot_instance = ServiceDocsDeviceReboot.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsDeviceReboot.to_json())

# convert the object into a dict
service_docs_device_reboot_dict = service_docs_device_reboot_instance.to_dict()
# create an instance of ServiceDocsDeviceReboot from a dict
service_docs_device_reboot_from_dict = ServiceDocsDeviceReboot.from_dict(service_docs_device_reboot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


