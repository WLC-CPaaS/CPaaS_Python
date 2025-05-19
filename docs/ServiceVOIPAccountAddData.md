# ServiceVOIPAccountAddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_id** | [**ModelsVOIPAccountOutputFullCallerid**](ModelsVOIPAccountOutputFullCallerid.md) |  | [optional] 
**do_not_disturb** | [**ModelsVOIPSharedDoNotDisturb**](ModelsVOIPSharedDoNotDisturb.md) |  | [optional] 
**music_on_hold** | [**ModelsVOIPAccountMusicOnHold**](ModelsVOIPAccountMusicOnHold.md) |  | [optional] 
**name** | **str** |  | 
**realm** | **str** |  | [optional] 
**timezone** | **str** |  | 

## Example

```python
from openapi_client.models.service_voip_account_add_data import ServiceVOIPAccountAddData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPAccountAddData from a JSON string
service_voip_account_add_data_instance = ServiceVOIPAccountAddData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPAccountAddData.to_json())

# convert the object into a dict
service_voip_account_add_data_dict = service_voip_account_add_data_instance.to_dict()
# create an instance of ServiceVOIPAccountAddData from a dict
service_voip_account_add_data_from_dict = ServiceVOIPAccountAddData.from_dict(service_voip_account_add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


