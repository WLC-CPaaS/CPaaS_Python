# TypesGeoLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent_code** | **str** | The two-letter code for the continent.  Amazon Route 53 supports the following continent codes:    - AF: Africa    - AN: Antarctica    - AS: Asia    - EU: Europe    - OC: Oceania    - NA: North America    - SA: South America  Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error. | [optional] 
**country_code** | **str** | For geolocation resource record sets, the two-letter code for a country.  Amazon Route 53 uses the two-letter country codes that are specified in [ISO standard 3166-1 alpha-2].  Route 53 also supports the country code UA for Ukraine.  [ISO standard 3166-1 alpha-2]: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 | [optional] 
**subdivision_code** | **str** | For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn&#39;t support any other values for SubdivisionCode . For a list of state abbreviations, see [Appendix B: Two–Letter State and Possession Abbreviations]on the United States Postal Service website.  If you specify subdivisioncode , you must also specify US for CountryCode .  [Appendix B: Two–Letter State and Possession Abbreviations]: https://pe.usps.com/text/pub28/28apb.htm | [optional] 

## Example

```python
from openapi_client.models.types_geo_location import TypesGeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TypesGeoLocation from a JSON string
types_geo_location_instance = TypesGeoLocation.from_json(json)
# print the JSON string representation of the object
print(TypesGeoLocation.to_json())

# convert the object into a dict
types_geo_location_dict = types_geo_location_instance.to_dict()
# create an instance of TypesGeoLocation from a dict
types_geo_location_from_dict = TypesGeoLocation.from_dict(types_geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


