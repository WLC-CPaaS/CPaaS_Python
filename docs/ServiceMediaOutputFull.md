# ServiceMediaOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_length** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**media_source** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**streamable** | **bool** |  | [optional] 
**tts** | [**ServiceTTS**](ServiceTTS.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_media_output_full import ServiceMediaOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMediaOutputFull from a JSON string
service_media_output_full_instance = ServiceMediaOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceMediaOutputFull.to_json())

# convert the object into a dict
service_media_output_full_dict = service_media_output_full_instance.to_dict()
# create an instance of ServiceMediaOutputFull from a dict
service_media_output_full_from_dict = ServiceMediaOutputFull.from_dict(service_media_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


