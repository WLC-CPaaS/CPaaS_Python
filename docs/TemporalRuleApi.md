# openapi_client.TemporalRuleApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_temporalrule_get**](TemporalRuleApi.md#v1_account_account_id_temporalrule_get) | **GET** /v1/account/{accountID}/temporalrule | Get Temporal Rule List
[**v1_account_account_id_temporalrule_post**](TemporalRuleApi.md#v1_account_account_id_temporalrule_post) | **POST** /v1/account/{accountID}/temporalrule | Create Temporal Rule
[**v1_account_account_id_temporalrule_temporal_rule_id_delete**](TemporalRuleApi.md#v1_account_account_id_temporalrule_temporal_rule_id_delete) | **DELETE** /v1/account/{accountID}/temporalrule/{temporalRuleID} | Delete Temporal Rule
[**v1_account_account_id_temporalrule_temporal_rule_id_get**](TemporalRuleApi.md#v1_account_account_id_temporalrule_temporal_rule_id_get) | **GET** /v1/account/{accountID}/temporalrule/{temporalRuleID} | Get Temporal Rule Details
[**v1_account_account_id_temporalrule_temporal_rule_id_put**](TemporalRuleApi.md#v1_account_account_id_temporalrule_temporal_rule_id_put) | **PUT** /v1/account/{accountID}/temporalrule/{temporalRuleID} | Update Temporal Rule


# **v1_account_account_id_temporalrule_get**
> ServiceDocsTemporalRuleGetAll v1_account_account_id_temporalrule_get(account_id, start_key=start_key, page_size=page_size)

Get Temporal Rule List

Access all temporal rules for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_get_all import ServiceDocsTemporalRuleGetAll
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
    api_instance = openapi_client.TemporalRuleApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Temporal Rule List
        api_response = api_instance.v1_account_account_id_temporalrule_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of TemporalRuleApi->v1_account_account_id_temporalrule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleApi->v1_account_account_id_temporalrule_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsTemporalRuleGetAll**](ServiceDocsTemporalRuleGetAll.md)

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

# **v1_account_account_id_temporalrule_post**
> ServiceDocsTemporalRuleGetSingle v1_account_account_id_temporalrule_post(account_id, temporalrule)

Create Temporal Rule

Create temporal rules for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_get_single import ServiceDocsTemporalRuleGetSingle
from openapi_client.models.service_voip_temporal_rule_add_edit2 import ServiceVOIPTemporalRuleAddEdit2
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
    api_instance = openapi_client.TemporalRuleApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alphanumeric
    temporalrule = openapi_client.ServiceVOIPTemporalRuleAddEdit2() # ServiceVOIPTemporalRuleAddEdit2 | payload fields

    try:
        # Create Temporal Rule
        api_response = api_instance.v1_account_account_id_temporalrule_post(account_id, temporalrule)
        print("The response of TemporalRuleApi->v1_account_account_id_temporalrule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleApi->v1_account_account_id_temporalrule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alphanumeric | 
 **temporalrule** | [**ServiceVOIPTemporalRuleAddEdit2**](ServiceVOIPTemporalRuleAddEdit2.md)| payload fields | 

### Return type

[**ServiceDocsTemporalRuleGetSingle**](ServiceDocsTemporalRuleGetSingle.md)

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

# **v1_account_account_id_temporalrule_temporal_rule_id_delete**
> ServiceDocsTemporalRuleGetSingle v1_account_account_id_temporalrule_temporal_rule_id_delete(account_id, temporal_rule_id)

Delete Temporal Rule

Remove a temporal rule from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_get_single import ServiceDocsTemporalRuleGetSingle
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
    api_instance = openapi_client.TemporalRuleApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_id = 'temporal_rule_id_example' # str | temporal rule ID, 32 alpha numeric

    try:
        # Delete Temporal Rule
        api_response = api_instance.v1_account_account_id_temporalrule_temporal_rule_id_delete(account_id, temporal_rule_id)
        print("The response of TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_id** | **str**| temporal rule ID, 32 alpha numeric | 

### Return type

[**ServiceDocsTemporalRuleGetSingle**](ServiceDocsTemporalRuleGetSingle.md)

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

# **v1_account_account_id_temporalrule_temporal_rule_id_get**
> ServiceDocsTemporalRuleGetSingle v1_account_account_id_temporalrule_temporal_rule_id_get(account_id, temporal_rule_id)

Get Temporal Rule Details

View details about individual time rules.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_get_single import ServiceDocsTemporalRuleGetSingle
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
    api_instance = openapi_client.TemporalRuleApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_id = 'temporal_rule_id_example' # str | Temporal Rule ID, 32 alpha numeric

    try:
        # Get Temporal Rule Details
        api_response = api_instance.v1_account_account_id_temporalrule_temporal_rule_id_get(account_id, temporal_rule_id)
        print("The response of TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_id** | **str**| Temporal Rule ID, 32 alpha numeric | 

### Return type

[**ServiceDocsTemporalRuleGetSingle**](ServiceDocsTemporalRuleGetSingle.md)

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

# **v1_account_account_id_temporalrule_temporal_rule_id_put**
> ServiceDocsTemporalRuleGetSingle v1_account_account_id_temporalrule_temporal_rule_id_put(account_id, temporal_rule_id, req_body)

Update Temporal Rule

Edit the existing temporal rules in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_temporal_rule_get_single import ServiceDocsTemporalRuleGetSingle
from openapi_client.models.service_voip_temporal_rule_add_edit2 import ServiceVOIPTemporalRuleAddEdit2
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
    api_instance = openapi_client.TemporalRuleApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    temporal_rule_id = 'temporal_rule_id_example' # str | Temporal Rule ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPTemporalRuleAddEdit2() # ServiceVOIPTemporalRuleAddEdit2 | payload fields

    try:
        # Update Temporal Rule
        api_response = api_instance.v1_account_account_id_temporalrule_temporal_rule_id_put(account_id, temporal_rule_id, req_body)
        print("The response of TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporalRuleApi->v1_account_account_id_temporalrule_temporal_rule_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **temporal_rule_id** | **str**| Temporal Rule ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPTemporalRuleAddEdit2**](ServiceVOIPTemporalRuleAddEdit2.md)| payload fields | 

### Return type

[**ServiceDocsTemporalRuleGetSingle**](ServiceDocsTemporalRuleGetSingle.md)

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

