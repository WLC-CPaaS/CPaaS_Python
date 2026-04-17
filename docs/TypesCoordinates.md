# TypesCoordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **str** | Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).  This member is required. | [optional] 
**longitude** | **str** | Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).  This member is required. | [optional] 

## Example

```python
from openapi_client.models.types_coordinates import TypesCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of TypesCoordinates from a JSON string
types_coordinates_instance = TypesCoordinates.from_json(json)
# print the JSON string representation of the object
print(TypesCoordinates.to_json())

# convert the object into a dict
types_coordinates_dict = types_coordinates_instance.to_dict()
# create an instance of TypesCoordinates from a dict
types_coordinates_from_dict = TypesCoordinates.from_dict(types_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


