# ServiceVOIPAccountEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_id** | [**ModelsVOIPAccountOutputFullCallerid**](ModelsVOIPAccountOutputFullCallerid.md) |  | [optional] 
**do_not_disturb** | [**ModelsVOIPSharedDoNotDisturb**](ModelsVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**music_on_hold** | [**ModelsVOIPAccountMusicOnHold**](ModelsVOIPAccountMusicOnHold.md) |  | [optional] 
**name** | **str** |  | 
**timezone** | **str** |  | 

## Example

```python
from openapi_client.models.service_voip_account_edit_data import ServiceVOIPAccountEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPAccountEditData from a JSON string
service_voip_account_edit_data_instance = ServiceVOIPAccountEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPAccountEditData.to_json())

# convert the object into a dict
service_voip_account_edit_data_dict = service_voip_account_edit_data_instance.to_dict()
# create an instance of ServiceVOIPAccountEditData from a dict
service_voip_account_edit_data_from_dict = ServiceVOIPAccountEditData.from_dict(service_voip_account_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


