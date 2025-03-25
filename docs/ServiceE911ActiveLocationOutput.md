# ServiceE911ActiveLocationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_status** | [**ServiceE911ActiveLocationStatus**](ServiceE911ActiveLocationStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_active_location_output import ServiceE911ActiveLocationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911ActiveLocationOutput from a JSON string
service_e911_active_location_output_instance = ServiceE911ActiveLocationOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911ActiveLocationOutput.to_json())

# convert the object into a dict
service_e911_active_location_output_dict = service_e911_active_location_output_instance.to_dict()
# create an instance of ServiceE911ActiveLocationOutput from a dict
service_e911_active_location_output_from_dict = ServiceE911ActiveLocationOutput.from_dict(service_e911_active_location_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


