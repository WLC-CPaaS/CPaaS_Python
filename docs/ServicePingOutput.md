# ServicePingOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_ping_output import ServicePingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePingOutput from a JSON string
service_ping_output_instance = ServicePingOutput.from_json(json)
# print the JSON string representation of the object
print(ServicePingOutput.to_json())

# convert the object into a dict
service_ping_output_dict = service_ping_output_instance.to_dict()
# create an instance of ServicePingOutput from a dict
service_ping_output_from_dict = ServicePingOutput.from_dict(service_ping_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


