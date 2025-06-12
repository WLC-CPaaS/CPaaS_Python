# openapi_client.CallQueueManagementApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_callqueue_get**](CallQueueManagementApi.md#v1_account_account_id_callqueue_get) | **GET** /v1/account/{accountID}/callqueue | Get Call Queues
[**v1_account_account_id_callqueue_post**](CallQueueManagementApi.md#v1_account_account_id_callqueue_post) | **POST** /v1/account/{accountID}/callqueue | Create Call Queue
[**v1_account_account_id_callqueue_queue_id_delete**](CallQueueManagementApi.md#v1_account_account_id_callqueue_queue_id_delete) | **DELETE** /v1/account/{accountID}/callqueue/{queueID} | Delete Call Queue
[**v1_account_account_id_callqueue_queue_id_get**](CallQueueManagementApi.md#v1_account_account_id_callqueue_queue_id_get) | **GET** /v1/account/{accountID}/callqueue/{queueID} | Get Call Queue Details
[**v1_account_account_id_callqueue_queue_id_put**](CallQueueManagementApi.md#v1_account_account_id_callqueue_queue_id_put) | **PUT** /v1/account/{accountID}/callqueue/{queueID} | Update Call Queue
[**v1_account_account_id_callqueue_queue_id_status_get**](CallQueueManagementApi.md#v1_account_account_id_callqueue_queue_id_status_get) | **GET** /v1/account/{accountID}/callqueue/{queueID}/status | Get Call Queue Status
[**v1_account_account_id_queueroles_get**](CallQueueManagementApi.md#v1_account_account_id_queueroles_get) | **GET** /v1/account/{accountID}/queueroles | Get Queue Roles of Account
[**v1_account_account_id_queueroles_queue_id_post**](CallQueueManagementApi.md#v1_account_account_id_queueroles_queue_id_post) | **POST** /v1/account/{accountID}/queueroles/{queueID} | Assign Queue Role to Call Queue


# **v1_account_account_id_callqueue_get**
> ServiceDocsCallQueueGetAll v1_account_account_id_callqueue_get(account_id)

Get Call Queues

Retrieve call queue details for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_all import ServiceDocsCallQueueGetAll
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Call Queues
        api_response = api_instance.v1_account_account_id_callqueue_get(account_id)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallQueueGetAll**](ServiceDocsCallQueueGetAll.md)

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

# **v1_account_account_id_callqueue_post**
> ServiceDocsCallQueueGetSingle v1_account_account_id_callqueue_post(account_id, req_body)

Create Call Queue

Set up a call queue in an account for specific inbound calls.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_single import ServiceDocsCallQueueGetSingle
from openapi_client.models.service_voip_call_queue_add_edit_data import ServiceVOIPCallQueueAddEditData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueAddEditData() # ServiceVOIPCallQueueAddEditData | payload fields

    try:
        # Create Call Queue
        api_response = api_instance.v1_account_account_id_callqueue_post(account_id, req_body)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueAddEditData**](ServiceVOIPCallQueueAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsCallQueueGetSingle**](ServiceDocsCallQueueGetSingle.md)

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

# **v1_account_account_id_callqueue_queue_id_delete**
> ServiceDocsCallQueueGetSingle v1_account_account_id_callqueue_queue_id_delete(account_id, queue_id)

Delete Call Queue

Remove the call queue from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_single import ServiceDocsCallQueueGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    queue_id = 'queue_id_example' # str | Queue ID, 32 alpha numeric

    try:
        # Delete Call Queue
        api_response = api_instance.v1_account_account_id_callqueue_queue_id_delete(account_id, queue_id)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **queue_id** | **str**| Queue ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallQueueGetSingle**](ServiceDocsCallQueueGetSingle.md)

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

# **v1_account_account_id_callqueue_queue_id_get**
> ServiceDocsCallQueueGetSingle v1_account_account_id_callqueue_queue_id_get(account_id, queue_id)

Get Call Queue Details

Capture metadata about a specific queue, such as queue_type and agent_wrapup_time.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_single import ServiceDocsCallQueueGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    queue_id = 'queue_id_example' # str | Queue ID, 32 alpha numeric

    try:
        # Get Call Queue Details
        api_response = api_instance.v1_account_account_id_callqueue_queue_id_get(account_id, queue_id)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **queue_id** | **str**| Queue ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallQueueGetSingle**](ServiceDocsCallQueueGetSingle.md)

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

# **v1_account_account_id_callqueue_queue_id_put**
> ServiceDocsCallQueueGetSingle v1_account_account_id_callqueue_queue_id_put(account_id, queue_id, req_body)

Update Call Queue

Update the metadata mentioned above.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_single import ServiceDocsCallQueueGetSingle
from openapi_client.models.service_voip_call_queue_add_edit_data import ServiceVOIPCallQueueAddEditData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    queue_id = 'queue_id_example' # str | Queue ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueAddEditData() # ServiceVOIPCallQueueAddEditData | payload fields

    try:
        # Update Call Queue
        api_response = api_instance.v1_account_account_id_callqueue_queue_id_put(account_id, queue_id, req_body)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **queue_id** | **str**| Queue ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueAddEditData**](ServiceVOIPCallQueueAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsCallQueueGetSingle**](ServiceDocsCallQueueGetSingle.md)

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

# **v1_account_account_id_callqueue_queue_id_status_get**
> ServiceDocsCallQueueGetSingleStatus v1_account_account_id_callqueue_queue_id_status_get(account_id, queue_id)

Get Call Queue Status

Access the status of a call queue in an account, such as the number of available agents (recipients), estimated wait time, and number of active sessions.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_single_status import ServiceDocsCallQueueGetSingleStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    queue_id = 'queue_id_example' # str | Queue ID, 32 alpha numeric

    try:
        # Get Call Queue Status
        api_response = api_instance.v1_account_account_id_callqueue_queue_id_status_get(account_id, queue_id)
        print("The response of CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_callqueue_queue_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **queue_id** | **str**| Queue ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallQueueGetSingleStatus**](ServiceDocsCallQueueGetSingleStatus.md)

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

# **v1_account_account_id_queueroles_get**
> ServiceDocsCallQueueGetRoles v1_account_account_id_queueroles_get(account_id)

Get Queue Roles of Account

Obtain data about each queue role in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_get_roles import ServiceDocsCallQueueGetRoles
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Queue Roles of Account
        api_response = api_instance.v1_account_account_id_queueroles_get(account_id)
        print("The response of CallQueueManagementApi->v1_account_account_id_queueroles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_queueroles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallQueueGetRoles**](ServiceDocsCallQueueGetRoles.md)

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

# **v1_account_account_id_queueroles_queue_id_post**
> ServiceAPIResponse v1_account_account_id_queueroles_queue_id_post(account_id, queue_id, req_body)

Assign Queue Role to Call Queue

Assign roles to members in a call queue.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_call_queue_role_assign_data import ServiceVOIPCallQueueRoleAssignData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallQueueManagementApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    queue_id = 'queue_id_example' # str | Queue ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueRoleAssignData() # ServiceVOIPCallQueueRoleAssignData | payload fields

    try:
        # Assign Queue Role to Call Queue
        api_response = api_instance.v1_account_account_id_queueroles_queue_id_post(account_id, queue_id, req_body)
        print("The response of CallQueueManagementApi->v1_account_account_id_queueroles_queue_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueManagementApi->v1_account_account_id_queueroles_queue_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **queue_id** | **str**| Queue ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueRoleAssignData**](ServiceVOIPCallQueueRoleAssignData.md)| payload fields | 

### Return type

[**ServiceAPIResponse**](ServiceAPIResponse.md)

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

