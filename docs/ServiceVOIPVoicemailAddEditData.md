# ServiceVOIPVoicemailAddEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **str** |  | 
**media** | [**ServiceVoicemailMedia**](ServiceVoicemailMedia.md) |  | [optional] 
**media_extension** | **str** |  | [optional] 
**name** | **str** |  | 
**owner_id** | **str** |  | [optional] 
**pin** | **str** |  | [optional] 
**require_pin** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_voicemail_add_edit_data import ServiceVOIPVoicemailAddEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPVoicemailAddEditData from a JSON string
service_voip_voicemail_add_edit_data_instance = ServiceVOIPVoicemailAddEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPVoicemailAddEditData.to_json())

# convert the object into a dict
service_voip_voicemail_add_edit_data_dict = service_voip_voicemail_add_edit_data_instance.to_dict()
# create an instance of ServiceVOIPVoicemailAddEditData from a dict
service_voip_voicemail_add_edit_data_from_dict = ServiceVOIPVoicemailAddEditData.from_dict(service_voip_voicemail_add_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


