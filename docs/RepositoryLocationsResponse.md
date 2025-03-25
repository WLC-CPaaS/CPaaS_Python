# RepositoryLocationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.repository_locations_response import RepositoryLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryLocationsResponse from a JSON string
repository_locations_response_instance = RepositoryLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(RepositoryLocationsResponse.to_json())

# convert the object into a dict
repository_locations_response_dict = repository_locations_response_instance.to_dict()
# create an instance of RepositoryLocationsResponse from a dict
repository_locations_response_from_dict = RepositoryLocationsResponse.from_dict(repository_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


