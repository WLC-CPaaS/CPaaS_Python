# TypesResourceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see [Supported DNS Resource Record Types]in the Amazon Route 53 Developer Guide.  You can specify more than one value for all record types except CNAME and SOA .  If you&#39;re creating an alias resource record set, omit Value .  [Supported DNS Resource Record Types]: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html  This member is required. | [optional] 

## Example

```python
from openapi_client.models.types_resource_record import TypesResourceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResourceRecord from a JSON string
types_resource_record_instance = TypesResourceRecord.from_json(json)
# print the JSON string representation of the object
print(TypesResourceRecord.to_json())

# convert the object into a dict
types_resource_record_dict = types_resource_record_instance.to_dict()
# create an instance of TypesResourceRecord from a dict
types_resource_record_from_dict = TypesResourceRecord.from_dict(types_resource_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


