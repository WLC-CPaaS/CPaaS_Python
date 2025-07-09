# ServiceDocsE911ActiveLocationURIApiOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceE911LocationURI**](ServiceE911LocationURI.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_e911_active_location_uri_api_output import ServiceDocsE911ActiveLocationURIApiOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsE911ActiveLocationURIApiOutput from a JSON string
service_docs_e911_active_location_uri_api_output_instance = ServiceDocsE911ActiveLocationURIApiOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsE911ActiveLocationURIApiOutput.to_json())

# convert the object into a dict
service_docs_e911_active_location_uri_api_output_dict = service_docs_e911_active_location_uri_api_output_instance.to_dict()
# create an instance of ServiceDocsE911ActiveLocationURIApiOutput from a dict
service_docs_e911_active_location_uri_api_output_from_dict = ServiceDocsE911ActiveLocationURIApiOutput.from_dict(service_docs_e911_active_location_uri_api_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


