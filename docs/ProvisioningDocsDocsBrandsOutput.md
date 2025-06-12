# ProvisioningDocsDocsBrandsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelsBrand]**](ModelsBrand.md) |  | [optional] 
**next_start_key** | **str** | List Pagination: Used to get the next page of results. Will not exist if this is the last page. | [optional] 
**page_size** | **int** | List Pagination: The number of results returned in this page | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**start_key** | **str** | List Pagination: Code for paged results | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.provisioning_docs_docs_brands_output import ProvisioningDocsDocsBrandsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDocsDocsBrandsOutput from a JSON string
provisioning_docs_docs_brands_output_instance = ProvisioningDocsDocsBrandsOutput.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDocsDocsBrandsOutput.to_json())

# convert the object into a dict
provisioning_docs_docs_brands_output_dict = provisioning_docs_docs_brands_output_instance.to_dict()
# create an instance of ProvisioningDocsDocsBrandsOutput from a dict
provisioning_docs_docs_brands_output_from_dict = ProvisioningDocsDocsBrandsOutput.from_dict(provisioning_docs_docs_brands_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


