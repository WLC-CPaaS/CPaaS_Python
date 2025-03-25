# MenuInputData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**MenuOutputDetailMedia**](MenuOutputDetailMedia.md) | The media (prompt) parameters | [optional] 
**name** | **str** | A friendly name for the menu | 
**timeout** | **int** | The amount of time (in milliseconds) to wait for the caller to begin entering digits | [optional] 

## Example

```python
from openapi_client.models.menu_input_data import MenuInputData

# TODO update the JSON string below
json = "{}"
# create an instance of MenuInputData from a JSON string
menu_input_data_instance = MenuInputData.from_json(json)
# print the JSON string representation of the object
print(MenuInputData.to_json())

# convert the object into a dict
menu_input_data_dict = menu_input_data_instance.to_dict()
# create an instance of MenuInputData from a dict
menu_input_data_from_dict = MenuInputData.from_dict(menu_input_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


