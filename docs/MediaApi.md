# openapi_client.MediaApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_media_media_id_file_get**](MediaApi.md#v1_account_account_id_media_media_id_file_get) | **GET** /v1/account/{accountID}/media/{mediaID}/file | Get Media File
[**v1_account_account_id_media_media_id_file_post**](MediaApi.md#v1_account_account_id_media_media_id_file_post) | **POST** /v1/account/{accountID}/media/{mediaID}/file | Add Media File
[**v1_account_accountid_media_get**](MediaApi.md#v1_account_accountid_media_get) | **GET** /v1/account/{accountid}/media | Get Media List
[**v1_account_accountid_media_mediaid_delete**](MediaApi.md#v1_account_accountid_media_mediaid_delete) | **DELETE** /v1/account/{accountid}/media/{mediaid} | Delete Media
[**v1_account_accountid_media_mediaid_get**](MediaApi.md#v1_account_accountid_media_mediaid_get) | **GET** /v1/account/{accountid}/media/{mediaid} | Get Media Details
[**v1_account_accountid_media_post**](MediaApi.md#v1_account_accountid_media_post) | **POST** /v1/account/{accountid}/media | Create Media


# **v1_account_account_id_media_media_id_file_get**
> bytearray v1_account_account_id_media_media_id_file_get(account_id, media_id)

Get Media File

Gather data about the media objects in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.MediaApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    media_id = 'media_id_example' # str | Media ID, 32 alpha numeric

    try:
        # Get Media File
        api_response = api_instance.v1_account_account_id_media_media_id_file_get(account_id, media_id)
        print("The response of MediaApi->v1_account_account_id_media_media_id_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_account_id_media_media_id_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **media_id** | **str**| Media ID, 32 alpha numeric | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, audio/mp3, audio/mpeg, audio/mpeg3, audio/x-wav, audio/wav, audio/ogg, video/x-flv, video/h264, video/mpeg, video/quicktime, video/mp4, video/webm

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_media_media_id_file_post**
> ServiceDocsMediaGetSingle v1_account_account_id_media_media_id_file_post(account_id, media_id, file)

Add Media File

Include a media file that is connected to a media object in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_media_get_single import ServiceDocsMediaGetSingle
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
    api_instance = openapi_client.MediaApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    media_id = 'media_id_example' # str | Media ID, 32 alpha numeric
    file = None # bytearray | Media file

    try:
        # Add Media File
        api_response = api_instance.v1_account_account_id_media_media_id_file_post(account_id, media_id, file)
        print("The response of MediaApi->v1_account_account_id_media_media_id_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_account_id_media_media_id_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **media_id** | **str**| Media ID, 32 alpha numeric | 
 **file** | **bytearray**| Media file | 

### Return type

[**ServiceDocsMediaGetSingle**](ServiceDocsMediaGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_accountid_media_get**
> ServiceDocsMediaGetAll v1_account_accountid_media_get(accountid, start_key=start_key, page_size=page_size)

Get Media List

View all media files for an account in your organization.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_media_get_all import ServiceDocsMediaGetAll
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
    api_instance = openapi_client.MediaApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Media List
        api_response = api_instance.v1_account_accountid_media_get(accountid, start_key=start_key, page_size=page_size)
        print("The response of MediaApi->v1_account_accountid_media_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_accountid_media_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsMediaGetAll**](ServiceDocsMediaGetAll.md)

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

# **v1_account_accountid_media_mediaid_delete**
> ServiceDocsMediaGetSingle v1_account_accountid_media_mediaid_delete(accountid, mediaid)

Delete Media

Remove a media file that is no longer in use from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_media_get_single import ServiceDocsMediaGetSingle
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
    api_instance = openapi_client.MediaApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    mediaid = 'mediaid_example' # str | Device ID, 32 alpha numeric

    try:
        # Delete Media
        api_response = api_instance.v1_account_accountid_media_mediaid_delete(accountid, mediaid)
        print("The response of MediaApi->v1_account_accountid_media_mediaid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_accountid_media_mediaid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **mediaid** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocsMediaGetSingle**](ServiceDocsMediaGetSingle.md)

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

# **v1_account_accountid_media_mediaid_get**
> ServiceDocsMediaGetSingle v1_account_accountid_media_mediaid_get(accountid, mediaid)

Get Media Details

Permit users to view an account's specific media information.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_media_get_single import ServiceDocsMediaGetSingle
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
    api_instance = openapi_client.MediaApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    mediaid = 'mediaid_example' # str | Media ID, 32 alpha numeric

    try:
        # Get Media Details
        api_response = api_instance.v1_account_accountid_media_mediaid_get(accountid, mediaid)
        print("The response of MediaApi->v1_account_accountid_media_mediaid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_accountid_media_mediaid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **mediaid** | **str**| Media ID, 32 alpha numeric | 

### Return type

[**ServiceDocsMediaGetSingle**](ServiceDocsMediaGetSingle.md)

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

# **v1_account_accountid_media_post**
> ServiceDocsMediaGetSingle v1_account_accountid_media_post(accountid, media)

Create Media

Generate a media object to allow users to upload a media file in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_media_get_single import ServiceDocsMediaGetSingle
from openapi_client.models.service_voip_media_add_edit_data import ServiceVOIPMediaAddEditData
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
    api_instance = openapi_client.MediaApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    media = openapi_client.ServiceVOIPMediaAddEditData() # ServiceVOIPMediaAddEditData | Media creation or update payload

    try:
        # Create Media
        api_response = api_instance.v1_account_accountid_media_post(accountid, media)
        print("The response of MediaApi->v1_account_accountid_media_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->v1_account_accountid_media_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **media** | [**ServiceVOIPMediaAddEditData**](ServiceVOIPMediaAddEditData.md)| Media creation or update payload | 

### Return type

[**ServiceDocsMediaGetSingle**](ServiceDocsMediaGetSingle.md)

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

