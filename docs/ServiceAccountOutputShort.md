# ServiceAccountOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendants_count** | **int** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_account_output_short import ServiceAccountOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountOutputShort from a JSON string
service_account_output_short_instance = ServiceAccountOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountOutputShort.to_json())

# convert the object into a dict
service_account_output_short_dict = service_account_output_short_instance.to_dict()
# create an instance of ServiceAccountOutputShort from a dict
service_account_output_short_from_dict = ServiceAccountOutputShort.from_dict(service_account_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


