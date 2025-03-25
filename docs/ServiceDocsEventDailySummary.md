# ServiceDocsEventDailySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelEventDailySummary]**](ModelEventDailySummary.md) |  | [optional] 
**next_start_key** | **str** | List Pagination: Used to get the next page of results. Will not exist if this is the last page. | [optional] 
**page_size** | **int** | List Pagination: The number of results returned in this page | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**start_key** | **str** | List Pagination: Code for paged results | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_event_daily_summary import ServiceDocsEventDailySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsEventDailySummary from a JSON string
service_docs_event_daily_summary_instance = ServiceDocsEventDailySummary.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsEventDailySummary.to_json())

# convert the object into a dict
service_docs_event_daily_summary_dict = service_docs_event_daily_summary_instance.to_dict()
# create an instance of ServiceDocsEventDailySummary from a dict
service_docs_event_daily_summary_from_dict = ServiceDocsEventDailySummary.from_dict(service_docs_event_daily_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


