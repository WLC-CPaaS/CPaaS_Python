# ServiceE911StatusOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_status_output import ServiceE911StatusOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911StatusOutput from a JSON string
service_e911_status_output_instance = ServiceE911StatusOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911StatusOutput.to_json())

# convert the object into a dict
service_e911_status_output_dict = service_e911_status_output_instance.to_dict()
# create an instance of ServiceE911StatusOutput from a dict
service_e911_status_output_from_dict = ServiceE911StatusOutput.from_dict(service_e911_status_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


