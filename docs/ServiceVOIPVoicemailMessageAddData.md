# ServiceVOIPVoicemailMessageAddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_id_name** | **str** |  | [optional] 
**caller_id_number** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_voicemail_message_add_data import ServiceVOIPVoicemailMessageAddData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPVoicemailMessageAddData from a JSON string
service_voip_voicemail_message_add_data_instance = ServiceVOIPVoicemailMessageAddData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPVoicemailMessageAddData.to_json())

# convert the object into a dict
service_voip_voicemail_message_add_data_dict = service_voip_voicemail_message_add_data_instance.to_dict()
# create an instance of ServiceVOIPVoicemailMessageAddData from a dict
service_voip_voicemail_message_add_data_from_dict = ServiceVOIPVoicemailMessageAddData.from_dict(service_voip_voicemail_message_add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


