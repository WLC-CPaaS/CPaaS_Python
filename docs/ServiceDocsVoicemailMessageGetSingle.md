# ServiceDocsVoicemailMessageGetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceVoicemailMessageOutput**](ServiceVoicemailMessageOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_voicemail_message_get_single import ServiceDocsVoicemailMessageGetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsVoicemailMessageGetSingle from a JSON string
service_docs_voicemail_message_get_single_instance = ServiceDocsVoicemailMessageGetSingle.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsVoicemailMessageGetSingle.to_json())

# convert the object into a dict
service_docs_voicemail_message_get_single_dict = service_docs_voicemail_message_get_single_instance.to_dict()
# create an instance of ServiceDocsVoicemailMessageGetSingle from a dict
service_docs_voicemail_message_get_single_from_dict = ServiceDocsVoicemailMessageGetSingle.from_dict(service_docs_voicemail_message_get_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


