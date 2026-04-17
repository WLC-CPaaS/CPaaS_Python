# TypesGeoProximityLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**awsregion** | **str** | The Amazon Web Services Region the resource you are directing DNS traffic to, is in. | [optional] 
**bias** | **int** | The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.  To use Bias to change the size of the geographic region, specify the applicable value for the bias:    - To expand the size of the geographic region from which Route 53 routes   traffic to a resource, specify a positive integer from 1 to 99 for the bias.   Route 53 shrinks the size of adjacent regions.    - To shrink the size of the geographic region from which Route 53 routes   traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands   the size of adjacent regions. | [optional] 
**coordinates** | [**TypesCoordinates**](TypesCoordinates.md) | Contains the longitude and latitude for a geographic region. | [optional] 
**local_zone_group** | **str** | Specifies an Amazon Web Services Local Zone Group.  A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is us-east-1-bue-1a the Local Zone Group is us-east-1-bue-1 .  You can identify the Local Zones Group for a specific Local Zone by using the [describe-availability-zones] CLI command:  This command returns: \&quot;GroupName\&quot;: \&quot;us-west-2-den-1\&quot; , specifying that the Local Zone us-west-2-den-1a belongs to the Local Zone Group us-west-2-den-1 .  [describe-availability-zones]: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html | [optional] 

## Example

```python
from openapi_client.models.types_geo_proximity_location import TypesGeoProximityLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TypesGeoProximityLocation from a JSON string
types_geo_proximity_location_instance = TypesGeoProximityLocation.from_json(json)
# print the JSON string representation of the object
print(TypesGeoProximityLocation.to_json())

# convert the object into a dict
types_geo_proximity_location_dict = types_geo_proximity_location_instance.to_dict()
# create an instance of TypesGeoProximityLocation from a dict
types_geo_proximity_location_from_dict = TypesGeoProximityLocation.from_dict(types_geo_proximity_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


