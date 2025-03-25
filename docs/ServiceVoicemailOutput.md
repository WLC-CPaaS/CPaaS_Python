# ServiceVoicemailOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**mailbox** | **str** |  | [optional] 
**media** | [**ServiceVoicemailMedia**](ServiceVoicemailMedia.md) |  | [optional] 
**media_extension** | **str** |  | [optional] 
**messages** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**pin** | **str** |  | [optional] 
**require_pin** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voicemail_output import ServiceVoicemailOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVoicemailOutput from a JSON string
service_voicemail_output_instance = ServiceVoicemailOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceVoicemailOutput.to_json())

# convert the object into a dict
service_voicemail_output_dict = service_voicemail_output_instance.to_dict()
# create an instance of ServiceVoicemailOutput from a dict
service_voicemail_output_from_dict = ServiceVoicemailOutput.from_dict(service_voicemail_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


