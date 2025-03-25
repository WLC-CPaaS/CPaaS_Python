# ServiceAccountOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_recording** | [**ServiceVOIPAccountCallRecording**](ServiceVOIPAccountCallRecording.md) |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**music_on_hold** | [**ServiceVOIPAccountMusicOnHold**](ServiceVOIPAccountMusicOnHold.md) |  | [optional] 
**name** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_account_output import ServiceAccountOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountOutput from a JSON string
service_account_output_instance = ServiceAccountOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountOutput.to_json())

# convert the object into a dict
service_account_output_dict = service_account_output_instance.to_dict()
# create an instance of ServiceAccountOutput from a dict
service_account_output_from_dict = ServiceAccountOutput.from_dict(service_account_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


