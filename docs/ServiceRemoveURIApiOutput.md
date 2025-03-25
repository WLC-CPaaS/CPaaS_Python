# ServiceRemoveURIApiOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri_status** | [**ServiceE911LocationURIStatus**](ServiceE911LocationURIStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_remove_uri_api_output import ServiceRemoveURIApiOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRemoveURIApiOutput from a JSON string
service_remove_uri_api_output_instance = ServiceRemoveURIApiOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceRemoveURIApiOutput.to_json())

# convert the object into a dict
service_remove_uri_api_output_dict = service_remove_uri_api_output_instance.to_dict()
# create an instance of ServiceRemoveURIApiOutput from a dict
service_remove_uri_api_output_from_dict = ServiceRemoveURIApiOutput.from_dict(service_remove_uri_api_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


