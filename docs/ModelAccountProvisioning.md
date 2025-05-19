# ModelAccountProvisioning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**provisioning_url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_account_provisioning import ModelAccountProvisioning

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountProvisioning from a JSON string
model_account_provisioning_instance = ModelAccountProvisioning.from_json(json)
# print the JSON string representation of the object
print(ModelAccountProvisioning.to_json())

# convert the object into a dict
model_account_provisioning_dict = model_account_provisioning_instance.to_dict()
# create an instance of ModelAccountProvisioning from a dict
model_account_provisioning_from_dict = ModelAccountProvisioning.from_dict(model_account_provisioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


