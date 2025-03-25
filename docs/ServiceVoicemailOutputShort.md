# ServiceVoicemailOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**mailbox** | **str** |  | [optional] 
**messages** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voicemail_output_short import ServiceVoicemailOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVoicemailOutputShort from a JSON string
service_voicemail_output_short_instance = ServiceVoicemailOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceVoicemailOutputShort.to_json())

# convert the object into a dict
service_voicemail_output_short_dict = service_voicemail_output_short_instance.to_dict()
# create an instance of ServiceVoicemailOutputShort from a dict
service_voicemail_output_short_from_dict = ServiceVoicemailOutputShort.from_dict(service_voicemail_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


