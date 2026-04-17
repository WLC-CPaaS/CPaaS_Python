# TypesCidrRoutingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The CIDR collection ID.  This member is required. | [optional] 
**location_name** | **str** | The CIDR collection location name.  This member is required. | [optional] 

## Example

```python
from openapi_client.models.types_cidr_routing_config import TypesCidrRoutingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TypesCidrRoutingConfig from a JSON string
types_cidr_routing_config_instance = TypesCidrRoutingConfig.from_json(json)
# print the JSON string representation of the object
print(TypesCidrRoutingConfig.to_json())

# convert the object into a dict
types_cidr_routing_config_dict = types_cidr_routing_config_instance.to_dict()
# create an instance of TypesCidrRoutingConfig from a dict
types_cidr_routing_config_from_dict = TypesCidrRoutingConfig.from_dict(types_cidr_routing_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


