# ServiceVoicemailMessageOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** |  | [optional] 
**caller_id_name** | **str** |  | [optional] 
**caller_id_number** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**media_id** | **str** |  | [optional] 
**succeeded** | **List[str]** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voicemail_message_output import ServiceVoicemailMessageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVoicemailMessageOutput from a JSON string
service_voicemail_message_output_instance = ServiceVoicemailMessageOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceVoicemailMessageOutput.to_json())

# convert the object into a dict
service_voicemail_message_output_dict = service_voicemail_message_output_instance.to_dict()
# create an instance of ServiceVoicemailMessageOutput from a dict
service_voicemail_message_output_from_dict = ServiceVoicemailMessageOutput.from_dict(service_voicemail_message_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


