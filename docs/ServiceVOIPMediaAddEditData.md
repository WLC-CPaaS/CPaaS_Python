# ServiceVOIPMediaAddEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**media_source** | **str** |  | [optional] 
**name** | **str** |  | 
**tts** | [**ServiceTTS**](ServiceTTS.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_media_add_edit_data import ServiceVOIPMediaAddEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPMediaAddEditData from a JSON string
service_voip_media_add_edit_data_instance = ServiceVOIPMediaAddEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPMediaAddEditData.to_json())

# convert the object into a dict
service_voip_media_add_edit_data_dict = service_voip_media_add_edit_data_instance.to_dict()
# create an instance of ServiceVOIPMediaAddEditData from a dict
service_voip_media_add_edit_data_from_dict = ServiceVOIPMediaAddEditData.from_dict(service_voip_media_add_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


