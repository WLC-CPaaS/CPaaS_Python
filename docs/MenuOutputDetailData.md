# MenuOutputDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the menu | [optional] 
**media** | [**MenuOutputDetailMedia**](MenuOutputDetailMedia.md) | The media (prompt) parameters | [optional] 
**name** | **str** | A friendly name for the menu | [optional] 
**timeout** | **int** | The amount of time (in milliseconds) to wait for the caller to begin entering digits | [optional] 

## Example

```python
from openapi_client.models.menu_output_detail_data import MenuOutputDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOutputDetailData from a JSON string
menu_output_detail_data_instance = MenuOutputDetailData.from_json(json)
# print the JSON string representation of the object
print(MenuOutputDetailData.to_json())

# convert the object into a dict
menu_output_detail_data_dict = menu_output_detail_data_instance.to_dict()
# create an instance of MenuOutputDetailData from a dict
menu_output_detail_data_from_dict = MenuOutputDetailData.from_dict(menu_output_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


