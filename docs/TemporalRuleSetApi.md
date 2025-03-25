# openapi_client.TemporalRuleSetApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_temporalruleset_get**](TemporalRuleSetApi.md#v1_account_account_id_temporalruleset_get) | **GET** /v1/account/{accountID}/temporalruleset | Get Temporal Rule Set List
[**v1_account_account_id_temporalruleset_post**](TemporalRuleSetApi.md#v1_account_account_id_temporalruleset_post) | **POST** /v1/account/{accountID}/temporalruleset | Create Temporal Rule Set
[**v1_account_account_id_temporalruleset_temporal_rule_set_id_delete**](TemporalRuleSetApi.md#v1_account_account_id_temporalruleset_temporal_rule_set_id_delete) | **DELETE** /v1/account/{accountID}/temporalruleset/{temporalRuleSetID} | Delete Temporal Rule Set
[**v1_account_account_id_temporalruleset_temporal_rule_set_id_get**](TemporalRuleSetApi.md#v1_account_account_id_temporalruleset_temporal_rule_set_id_get) | **GET** /v1/account/{accountID}/temporalruleset/{temporalRuleSetID} | Get Temporal Rule Set Details
[**v1_account_account_id_temporalruleset_temporal_rule_set_id_put**](TemporalRuleSetApi.md#v1_account_account_id_temporalruleset_temporal_rule_set_id_put) | **PUT** /v1/account/{accountID}/temporalruleset/{temporalRuleSetID} | Update Temporal Rule Set


# **v1_account_account_id_temporalruleset_get**
> ServiceDocsTemporalRuleSetGetAll v1_account_account_id_temporalruleset_get(account_id, start_key=start_key, page_size=page_size)

Get Temporal Rule Set List

Access the temporal rule set list in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_set_get_all import ServiceDocsTemporalRuleSetGetAll
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemporalRuleSetApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Temporal Rule Set List
        api_response = api_instance.v1_account_account_id_temporalruleset_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of TemporalRuleSetApi->v1_account_account_id_temporalruleset_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleSetApi->v1_account_account_id_temporalruleset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsTemporalRuleSetGetAll**](ServiceDocsTemporalRuleSetGetAll.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_temporalruleset_post**
> ServiceDocsTemporalRuleSetGetSingle v1_account_account_id_temporalruleset_post(account_id, temporalruleset)

Create Temporal Rule Set

Develop a new temporal rule set for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_set_get_single import ServiceDocsTemporalRuleSetGetSingle
from openapi_client.models.service_voip_temporal_rule_set_add_edit_data import ServiceVOIPTemporalRuleSetAddEditData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemporalRuleSetApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alphanumeric
    temporalruleset = openapi_client.ServiceVOIPTemporalRuleSetAddEditData() # ServiceVOIPTemporalRuleSetAddEditData | payload fields

    try:
        # Create Temporal Rule Set
        api_response = api_instance.v1_account_account_id_temporalruleset_post(account_id, temporalruleset)
        print("The response of TemporalRuleSetApi->v1_account_account_id_temporalruleset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleSetApi->v1_account_account_id_temporalruleset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alphanumeric | 
 **temporalruleset** | [**ServiceVOIPTemporalRuleSetAddEditData**](ServiceVOIPTemporalRuleSetAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsTemporalRuleSetGetSingle**](ServiceDocsTemporalRuleSetGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_temporalruleset_temporal_rule_set_id_delete**
> ServiceDocsTemporalRuleSetGetSingle v1_account_account_id_temporalruleset_temporal_rule_set_id_delete(account_id, temporal_rule_set_id)

Delete Temporal Rule Set

Delete the temporal rule set from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_set_get_single import ServiceDocsTemporalRuleSetGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemporalRuleSetApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_set_id = 'temporal_rule_set_id_example' # str | temporal rule set ID, 32 alpha numeric

    try:
        # Delete Temporal Rule Set
        api_response = api_instance.v1_account_account_id_temporalruleset_temporal_rule_set_id_delete(account_id, temporal_rule_set_id)
        print("The response of TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_set_id** | **str**| temporal rule set ID, 32 alpha numeric | 

### Return type

[**ServiceDocsTemporalRuleSetGetSingle**](ServiceDocsTemporalRuleSetGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_temporalruleset_temporal_rule_set_id_get**
> ServiceDocsTemporalRuleSetGetSingle v1_account_account_id_temporalruleset_temporal_rule_set_id_get(account_id, temporal_rule_set_id)

Get Temporal Rule Set Details

Acquire details about a temporal rule set in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_set_get_single import ServiceDocsTemporalRuleSetGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemporalRuleSetApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_set_id = 'temporal_rule_set_id_example' # str | Temporal Ruleset ID, 32 alpha numeric

    try:
        # Get Temporal Rule Set Details
        api_response = api_instance.v1_account_account_id_temporalruleset_temporal_rule_set_id_get(account_id, temporal_rule_set_id)
        print("The response of TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_set_id** | **str**| Temporal Ruleset ID, 32 alpha numeric | 

### Return type

[**ServiceDocsTemporalRuleSetGetSingle**](ServiceDocsTemporalRuleSetGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_temporalruleset_temporal_rule_set_id_put**
> ServiceDocsTemporalRuleSetGetSingle v1_account_account_id_temporalruleset_temporal_rule_set_id_put(account_id, temporal_rule_set_id, req_body)

Update Temporal Rule Set

Efficiently adjust the temporal rule set in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_set_get_single import ServiceDocsTemporalRuleSetGetSingle
from openapi_client.models.service_voip_temporal_rule_set_add_edit_data import ServiceVOIPTemporalRuleSetAddEditData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemporalRuleSetApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_set_id = 'temporal_rule_set_id_example' # str | Temporal Ruleset ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPTemporalRuleSetAddEditData() # ServiceVOIPTemporalRuleSetAddEditData | payload fields

    try:
        # Update Temporal Rule Set
        api_response = api_instance.v1_account_account_id_temporalruleset_temporal_rule_set_id_put(account_id, temporal_rule_set_id, req_body)
        print("The response of TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleSetApi->v1_account_account_id_temporalruleset_temporal_rule_set_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_set_id** | **str**| Temporal Ruleset ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPTemporalRuleSetAddEditData**](ServiceVOIPTemporalRuleSetAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsTemporalRuleSetGetSingle**](ServiceDocsTemporalRuleSetGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

