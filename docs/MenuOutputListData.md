# MenuOutputListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | Features used in this menu | [optional] 
**flags** | **List[str]** | Flags set by external applications | [optional] 
**id** | **str** | ID of the menu | [optional] 
**name** | **str** | A friendly name for the menu | [optional] 

## Example

```python
from openapi_client.models.menu_output_list_data import MenuOutputListData

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOutputListData from a JSON string
menu_output_list_data_instance = MenuOutputListData.from_json(json)
# print the JSON string representation of the object
print(MenuOutputListData.to_json())

# convert the object into a dict
menu_output_list_data_dict = menu_output_list_data_instance.to_dict()
# create an instance of MenuOutputListData from a dict
menu_output_list_data_from_dict = MenuOutputListData.from_dict(menu_output_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


