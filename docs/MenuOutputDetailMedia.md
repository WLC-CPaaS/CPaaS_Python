# MenuOutputDetailMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**greeting** | **str** | The ID of a media object that should be used as the menu greeting | [optional] 
**invalid_media** | **object** | When the collected digits don&#39;t result in a match or hunt this media can be played | [optional] 
**transfer_media** | **object** | When a call is transferred from the menu, either after all retries exhausted or a successful hunt, this media can be played | [optional] 

## Example

```python
from openapi_client.models.menu_output_detail_media import MenuOutputDetailMedia

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOutputDetailMedia from a JSON string
menu_output_detail_media_instance = MenuOutputDetailMedia.from_json(json)
# print the JSON string representation of the object
print(MenuOutputDetailMedia.to_json())

# convert the object into a dict
menu_output_detail_media_dict = menu_output_detail_media_instance.to_dict()
# create an instance of MenuOutputDetailMedia from a dict
menu_output_detail_media_from_dict = MenuOutputDetailMedia.from_dict(menu_output_detail_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


