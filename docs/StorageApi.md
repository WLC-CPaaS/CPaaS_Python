# openapi_client.StorageApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_storage_delete**](StorageApi.md#v1_account_account_id_storage_delete) | **DELETE** /v1/account/{accountID}/storage | Delete Storage
[**v1_account_account_id_storage_get**](StorageApi.md#v1_account_account_id_storage_get) | **GET** /v1/account/{accountID}/storage | Get Storage Details
[**v1_account_account_id_storage_post**](StorageApi.md#v1_account_account_id_storage_post) | **POST** /v1/account/{accountID}/storage | Create Storage
[**v1_account_account_id_storage_put**](StorageApi.md#v1_account_account_id_storage_put) | **PUT** /v1/account/{accountID}/storage | Update Storage


# **v1_account_account_id_storage_delete**
> ServiceDocsStorageGet v1_account_account_id_storage_delete(account_id)

Delete Storage

Delete items that are stored in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_storage_get import ServiceDocsStorageGet
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
    api_instance = openapi_client.StorageApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Delete Storage
        api_response = api_instance.v1_account_account_id_storage_delete(account_id)
        print("The response of StorageApi->v1_account_account_id_storage_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->v1_account_account_id_storage_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsStorageGet**](ServiceDocsStorageGet.md)

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

# **v1_account_account_id_storage_get**
> ServiceDocsStorageGet v1_account_account_id_storage_get(account_id)

Get Storage Details

Retrieve storage details for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_storage_get import ServiceDocsStorageGet
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
    api_instance = openapi_client.StorageApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Storage Details
        api_response = api_instance.v1_account_account_id_storage_get(account_id)
        print("The response of StorageApi->v1_account_account_id_storage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->v1_account_account_id_storage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsStorageGet**](ServiceDocsStorageGet.md)

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

# **v1_account_account_id_storage_post**
> ServiceDocsStorageGet v1_account_account_id_storage_post(account_id, req_body)

Create Storage

Create storage in an account for voicemails, call recordings, faxes, etc.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_storage_get import ServiceDocsStorageGet
from openapi_client.models.service_voip_storage_add_edit_data import ServiceVOIPStorageAddEditData
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
    api_instance = openapi_client.StorageApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPStorageAddEditData() # ServiceVOIPStorageAddEditData | payload fields

    try:
        # Create Storage
        api_response = api_instance.v1_account_account_id_storage_post(account_id, req_body)
        print("The response of StorageApi->v1_account_account_id_storage_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->v1_account_account_id_storage_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPStorageAddEditData**](ServiceVOIPStorageAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsStorageGet**](ServiceDocsStorageGet.md)

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

# **v1_account_account_id_storage_put**
> ServiceDocsStorageGet v1_account_account_id_storage_put(account_id, req_body)

Update Storage

Modify the names of metadata to make it easier to locate (e.g., change the name of voicemail_storage to voicemail_and_callrecordings_storage, etc.).

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_storage_get import ServiceDocsStorageGet
from openapi_client.models.service_voip_storage_add_edit_data import ServiceVOIPStorageAddEditData
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
    api_instance = openapi_client.StorageApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPStorageAddEditData() # ServiceVOIPStorageAddEditData | payload fields

    try:
        # Update Storage
        api_response = api_instance.v1_account_account_id_storage_put(account_id, req_body)
        print("The response of StorageApi->v1_account_account_id_storage_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->v1_account_account_id_storage_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPStorageAddEditData**](ServiceVOIPStorageAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsStorageGet**](ServiceDocsStorageGet.md)

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

