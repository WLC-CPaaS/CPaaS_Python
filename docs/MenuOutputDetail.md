# MenuOutputDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MenuOutputDetailData**](MenuOutputDetailData.md) | Data Payload | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.menu_output_detail import MenuOutputDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOutputDetail from a JSON string
menu_output_detail_instance = MenuOutputDetail.from_json(json)
# print the JSON string representation of the object
print(MenuOutputDetail.to_json())

# convert the object into a dict
menu_output_detail_dict = menu_output_detail_instance.to_dict()
# create an instance of MenuOutputDetail from a dict
menu_output_detail_from_dict = MenuOutputDetail.from_dict(menu_output_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


