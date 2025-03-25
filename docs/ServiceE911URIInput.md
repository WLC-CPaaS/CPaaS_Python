# ServiceE911URIInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_name** | **str** |  | 
**uri** | **str** |  | 

## Example

```python
from openapi_client.models.service_e911_uri_input import ServiceE911URIInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911URIInput from a JSON string
service_e911_uri_input_instance = ServiceE911URIInput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911URIInput.to_json())

# convert the object into a dict
service_e911_uri_input_dict = service_e911_uri_input_instance.to_dict()
# create an instance of ServiceE911URIInput from a dict
service_e911_uri_input_from_dict = ServiceE911URIInput.from_dict(service_e911_uri_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


