# ServiceDocsE911ValidateLocationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceE911ValidateLocationOutput**](ServiceE911ValidateLocationOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_e911_validate_location_output import ServiceDocsE911ValidateLocationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsE911ValidateLocationOutput from a JSON string
service_docs_e911_validate_location_output_instance = ServiceDocsE911ValidateLocationOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsE911ValidateLocationOutput.to_json())

# convert the object into a dict
service_docs_e911_validate_location_output_dict = service_docs_e911_validate_location_output_instance.to_dict()
# create an instance of ServiceDocsE911ValidateLocationOutput from a dict
service_docs_e911_validate_location_output_from_dict = ServiceDocsE911ValidateLocationOutput.from_dict(service_docs_e911_validate_location_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


