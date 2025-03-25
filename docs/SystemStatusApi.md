# openapi_client.SystemStatusApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ping_get**](SystemStatusApi.md#v1_ping_get) | **GET** /v1/ping | Ping Backend
[**v1_pingseccognito_get**](SystemStatusApi.md#v1_pingseccognito_get) | **GET** /v1/pingseccognito | Ping Cognito
[**v1_system_status_get**](SystemStatusApi.md#v1_system_status_get) | **GET** /v1/system_status | Get System Status


# **v1_ping_get**
> ServiceDocsPingGet v1_ping_get()

Ping Backend

Get the ping message.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_ping_get import ServiceDocsPingGet
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
    api_instance = openapi_client.SystemStatusApi(api_client)

    try:
        # Ping Backend
        api_response = api_instance.v1_ping_get()
        print("The response of SystemStatusApi->v1_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->v1_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceDocsPingGet**](ServiceDocsPingGet.md)

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

# **v1_pingseccognito_get**
> ServiceDocsPingGet v1_pingseccognito_get()

Ping Cognito

Get a secure ping message.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_ping_get import ServiceDocsPingGet
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
    api_instance = openapi_client.SystemStatusApi(api_client)

    try:
        # Ping Cognito
        api_response = api_instance.v1_pingseccognito_get()
        print("The response of SystemStatusApi->v1_pingseccognito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->v1_pingseccognito_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceDocsPingGet**](ServiceDocsPingGet.md)

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

# **v1_system_status_get**
> ServiceDocsSystemStatusGetSingle v1_system_status_get()

Get System Status

Get the system status.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_system_status_get_single import ServiceDocsSystemStatusGetSingle
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
    api_instance = openapi_client.SystemStatusApi(api_client)

    try:
        # Get System Status
        api_response = api_instance.v1_system_status_get()
        print("The response of SystemStatusApi->v1_system_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->v1_system_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceDocsSystemStatusGetSingle**](ServiceDocsSystemStatusGetSingle.md)

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

