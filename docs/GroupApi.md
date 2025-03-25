# openapi_client.GroupApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_group_get**](GroupApi.md#v1_account_account_id_group_get) | **GET** /v1/account/{accountID}/group | Get Group List
[**v1_account_account_id_group_group_id_delete**](GroupApi.md#v1_account_account_id_group_group_id_delete) | **DELETE** /v1/account/{accountID}/group/{groupID} | Delete Group
[**v1_account_account_id_group_group_id_get**](GroupApi.md#v1_account_account_id_group_group_id_get) | **GET** /v1/account/{accountID}/group/{groupID} | Get Group Details
[**v1_account_account_id_group_group_id_put**](GroupApi.md#v1_account_account_id_group_group_id_put) | **PUT** /v1/account/{accountID}/group/{groupID} | Update Group
[**v1_account_account_id_group_post**](GroupApi.md#v1_account_account_id_group_post) | **POST** /v1/account/{accountID}/group | Create Group


# **v1_account_account_id_group_get**
> ServiceDocGroupGetAll v1_account_account_id_group_get(account_id, start_key=start_key, page_size=page_size)

Get Group List

Get a list of groups associated with an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_group_get_all import ServiceDocGroupGetAll
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
    api_instance = openapi_client.GroupApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Group List
        api_response = api_instance.v1_account_account_id_group_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of GroupApi->v1_account_account_id_group_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_account_account_id_group_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocGroupGetAll**](ServiceDocGroupGetAll.md)

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

# **v1_account_account_id_group_group_id_delete**
> ServiceDocGroupGetSingle v1_account_account_id_group_group_id_delete(account_id, group_id)

Delete Group

Delete a call group in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_group_get_single import ServiceDocGroupGetSingle
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
    api_instance = openapi_client.GroupApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    group_id = 'group_id_example' # str | group ID, 32 alpha numeric

    try:
        # Delete Group
        api_response = api_instance.v1_account_account_id_group_group_id_delete(account_id, group_id)
        print("The response of GroupApi->v1_account_account_id_group_group_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_account_account_id_group_group_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **group_id** | **str**| group ID, 32 alpha numeric | 

### Return type

[**ServiceDocGroupGetSingle**](ServiceDocGroupGetSingle.md)

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

# **v1_account_account_id_group_group_id_get**
> ServiceDocGroupGetSingle v1_account_account_id_group_group_id_get(account_id, group_id)

Get Group Details

Access details about a single group within an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_group_get_single import ServiceDocGroupGetSingle
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
    api_instance = openapi_client.GroupApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    group_id = 'group_id_example' # str | Group ID, 32 alpha numeric

    try:
        # Get Group Details
        api_response = api_instance.v1_account_account_id_group_group_id_get(account_id, group_id)
        print("The response of GroupApi->v1_account_account_id_group_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_account_account_id_group_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **group_id** | **str**| Group ID, 32 alpha numeric | 

### Return type

[**ServiceDocGroupGetSingle**](ServiceDocGroupGetSingle.md)

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

# **v1_account_account_id_group_group_id_put**
> ServiceDocGroupGetSingle v1_account_account_id_group_group_id_put(account_id, group_id, req_body)

Update Group

Modify the name, settings and other information for a group within an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_group_get_single import ServiceDocGroupGetSingle
from openapi_client.models.service_voip_group_add_edit2 import ServiceVOIPGroupAddEdit2
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
    api_instance = openapi_client.GroupApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    group_id = 'group_id_example' # str | Group ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPGroupAddEdit2() # ServiceVOIPGroupAddEdit2 | payload fields

    try:
        # Update Group
        api_response = api_instance.v1_account_account_id_group_group_id_put(account_id, group_id, req_body)
        print("The response of GroupApi->v1_account_account_id_group_group_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_account_account_id_group_group_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **group_id** | **str**| Group ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPGroupAddEdit2**](ServiceVOIPGroupAddEdit2.md)| payload fields | 

### Return type

[**ServiceDocGroupGetSingle**](ServiceDocGroupGetSingle.md)

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

# **v1_account_account_id_group_post**
> ServiceDocGroupGetSingle v1_account_account_id_group_post(account_id, group)

Create Group

Provide an additional resource by adding a group list to an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_group_get_single import ServiceDocGroupGetSingle
from openapi_client.models.service_voip_group_add_edit2 import ServiceVOIPGroupAddEdit2
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
    api_instance = openapi_client.GroupApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    group = openapi_client.ServiceVOIPGroupAddEdit2() # ServiceVOIPGroupAddEdit2 | group fields

    try:
        # Create Group
        api_response = api_instance.v1_account_account_id_group_post(account_id, group)
        print("The response of GroupApi->v1_account_account_id_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_account_account_id_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **group** | [**ServiceVOIPGroupAddEdit2**](ServiceVOIPGroupAddEdit2.md)| group fields | 

### Return type

[**ServiceDocGroupGetSingle**](ServiceDocGroupGetSingle.md)

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

