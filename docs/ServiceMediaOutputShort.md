# ServiceMediaOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_prompt** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 
**media_source** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_media_output_short import ServiceMediaOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMediaOutputShort from a JSON string
service_media_output_short_instance = ServiceMediaOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceMediaOutputShort.to_json())

# convert the object into a dict
service_media_output_short_dict = service_media_output_short_instance.to_dict()
# create an instance of ServiceMediaOutputShort from a dict
service_media_output_short_from_dict = ServiceMediaOutputShort.from_dict(service_media_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


