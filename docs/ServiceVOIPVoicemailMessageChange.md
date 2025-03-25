# ServiceVOIPVoicemailMessageChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** |  | [optional] 
**source_id** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_voicemail_message_change import ServiceVOIPVoicemailMessageChange

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPVoicemailMessageChange from a JSON string
service_voip_voicemail_message_change_instance = ServiceVOIPVoicemailMessageChange.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPVoicemailMessageChange.to_json())

# convert the object into a dict
service_voip_voicemail_message_change_dict = service_voip_voicemail_message_change_instance.to_dict()
# create an instance of ServiceVOIPVoicemailMessageChange from a dict
service_voip_voicemail_message_change_from_dict = ServiceVOIPVoicemailMessageChange.from_dict(service_voip_voicemail_message_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


