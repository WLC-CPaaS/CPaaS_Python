# openapi_client.VoicemailApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_voicemail_get**](VoicemailApi.md#v1_account_account_id_voicemail_get) | **GET** /v1/account/{accountID}/voicemail | Get Voicemail Box List
[**v1_account_account_id_voicemail_post**](VoicemailApi.md#v1_account_account_id_voicemail_post) | **POST** /v1/account/{accountID}/voicemail | Create Voicemail Box
[**v1_account_account_id_voicemail_voicemail_id_delete**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_delete) | **DELETE** /v1/account/{accountID}/voicemail/{voicemailID} | Delete Voicemail Box
[**v1_account_account_id_voicemail_voicemail_id_get**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_get) | **GET** /v1/account/{accountID}/voicemail/{voicemailID} | Get Voicemail Box Details
[**v1_account_account_id_voicemail_voicemail_id_message_get**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_get) | **GET** /v1/account/{accountID}/voicemail/{voicemailID}/message | Get Voicemail Message List
[**v1_account_account_id_voicemail_voicemail_id_message_message_id_delete**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_message_id_delete) | **DELETE** /v1/account/{accountID}/voicemail/{voicemailID}/message/{messageID} | Delete Voicemail Message
[**v1_account_account_id_voicemail_voicemail_id_message_message_id_get**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_message_id_get) | **GET** /v1/account/{accountID}/voicemail/{voicemailID}/message/{messageID} | Get Voicemail Message Details
[**v1_account_account_id_voicemail_voicemail_id_message_message_id_put**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_message_id_put) | **PUT** /v1/account/{accountID}/voicemail/{voicemailID}/message/{messageID} | Update Voicemail Message
[**v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get) | **GET** /v1/account/{accountID}/voicemail/{voicemailID}/message/{messageID}/raw | Get Voicemail Message File
[**v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post) | **POST** /v1/account/{accountID}/voicemail/{voicemailID}/message/{messageID}/raw | Add Voicemail Message File
[**v1_account_account_id_voicemail_voicemail_id_message_post**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_message_post) | **POST** /v1/account/{accountID}/voicemail/{voicemailID}/message | Create Voicemail Message
[**v1_account_account_id_voicemail_voicemail_id_put**](VoicemailApi.md#v1_account_account_id_voicemail_voicemail_id_put) | **PUT** /v1/account/{accountID}/voicemail/{voicemailID} | Update Voicemail Box


# **v1_account_account_id_voicemail_get**
> ServiceDocsVoicemailGetAll v1_account_account_id_voicemail_get(account_id, start_key=start_key, page_size=page_size)

Get Voicemail Box List

List all voicemail boxes in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_get_all import ServiceDocsVoicemailGetAll
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Voicemail Box List
        api_response = api_instance.v1_account_account_id_voicemail_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsVoicemailGetAll**](ServiceDocsVoicemailGetAll.md)

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

# **v1_account_account_id_voicemail_post**
> ServiceDocsVoicemailGetSingle v1_account_account_id_voicemail_post(account_id, voicemail)

Create Voicemail Box

Create a voicemail box for receiving and storing voicemail messages.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_get_single import ServiceDocsVoicemailGetSingle
from openapi_client.models.service_voip_voicemail_add_edit_data import ServiceVOIPVoicemailAddEditData
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | account ID, 32 alphanumeric
    voicemail = openapi_client.ServiceVOIPVoicemailAddEditData() # ServiceVOIPVoicemailAddEditData | voicemail payload fields

    try:
        # Create Voicemail Box
        api_response = api_instance.v1_account_account_id_voicemail_post(account_id, voicemail)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID, 32 alphanumeric | 
 **voicemail** | [**ServiceVOIPVoicemailAddEditData**](ServiceVOIPVoicemailAddEditData.md)| voicemail payload fields | 

### Return type

[**ServiceDocsVoicemailGetSingle**](ServiceDocsVoicemailGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_delete**
> ServiceDocsVoicemailGetSingle v1_account_account_id_voicemail_voicemail_id_delete(account_id, voicemail_id)

Delete Voicemail Box

Delete a voicemail box in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_get_single import ServiceDocsVoicemailGetSingle
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric

    try:
        # Delete Voicemail Box
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_delete(account_id, voicemail_id)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 

### Return type

[**ServiceDocsVoicemailGetSingle**](ServiceDocsVoicemailGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_get**
> ServiceDocsVoicemailGetSingle v1_account_account_id_voicemail_voicemail_id_get(account_id, voicemail_id)

Get Voicemail Box Details

Get information about a single voicemail box.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_get_single import ServiceDocsVoicemailGetSingle
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric

    try:
        # Get Voicemail Box Details
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_get(account_id, voicemail_id)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 

### Return type

[**ServiceDocsVoicemailGetSingle**](ServiceDocsVoicemailGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_message_get**
> ServiceDocsVoicemailMessageGetAll v1_account_account_id_voicemail_voicemail_id_message_get(account_id, voicemail_id, start_key=start_key, page_size=page_size)

Get Voicemail Message List

Get a list of voicemail messages from an account's voicemail box.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_message_get_all import ServiceDocsVoicemailMessageGetAll
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | voicemail ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Voicemail Message List
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_get(account_id, voicemail_id, start_key=start_key, page_size=page_size)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| voicemail ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsVoicemailMessageGetAll**](ServiceDocsVoicemailMessageGetAll.md)

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

# **v1_account_account_id_voicemail_voicemail_id_message_message_id_delete**
> ServiceDocsVoicemailMessageGetSingle v1_account_account_id_voicemail_voicemail_id_message_message_id_delete(account_id, voicemail_id, message_id)

Delete Voicemail Message

Delete a voicemail message from a voicemail box in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_message_get_single import ServiceDocsVoicemailMessageGetSingle
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric
    message_id = 'message_id_example' # str | message ID, 32 alpha numeric

    try:
        # Delete Voicemail Message
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_message_id_delete(account_id, voicemail_id, message_id)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 
 **message_id** | **str**| message ID, 32 alpha numeric | 

### Return type

[**ServiceDocsVoicemailMessageGetSingle**](ServiceDocsVoicemailMessageGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_message_message_id_get**
> ServiceDocsVoicemailMessageGetSingle v1_account_account_id_voicemail_voicemail_id_message_message_id_get(account_id, voicemail_id, message_id)

Get Voicemail Message Details

Retrieve the container details of an individual voicemail message. This includes a reference to the audio file, but not the message itself.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_message_get_single import ServiceDocsVoicemailMessageGetSingle
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric
    message_id = 'message_id_example' # str | Message ID, 39 (yyyymm-<32 id>)

    try:
        # Get Voicemail Message Details
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_message_id_get(account_id, voicemail_id, message_id)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 
 **message_id** | **str**| Message ID, 39 (yyyymm-&lt;32 id&gt;) | 

### Return type

[**ServiceDocsVoicemailMessageGetSingle**](ServiceDocsVoicemailMessageGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_message_message_id_put**
> ServiceDocsVoicemailMessageGetSingle v1_account_account_id_voicemail_voicemail_id_message_message_id_put(account_id, voicemail_id, message_id, req_body)

Update Voicemail Message

Copy or move a voicemail message to a different folder in the same voicemail box or move the message to a separate voicemail box.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_message_get_single import ServiceDocsVoicemailMessageGetSingle
from openapi_client.models.service_voip_voicemail_message_change import ServiceVOIPVoicemailMessageChange
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric
    message_id = 'message_id_example' # str | Message ID, 39 (yyyymm-<32 id>)
    req_body = openapi_client.ServiceVOIPVoicemailMessageChange() # ServiceVOIPVoicemailMessageChange | payload fields

    try:
        # Update Voicemail Message
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_message_id_put(account_id, voicemail_id, message_id, req_body)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 
 **message_id** | **str**| Message ID, 39 (yyyymm-&lt;32 id&gt;) | 
 **req_body** | [**ServiceVOIPVoicemailMessageChange**](ServiceVOIPVoicemailMessageChange.md)| payload fields | 

### Return type

[**ServiceDocsVoicemailMessageGetSingle**](ServiceDocsVoicemailMessageGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get**
> bytearray v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get(account_id, voicemail_id, message_id)

Get Voicemail Message File

Get the original audio content of a specific voicemail message identified by its unique ID within an account's voicemail box. URL Param \"voicemailID\" is a unique 32-character alphanumeric identifier assigned by the system, which refers to a specific voicemail box. URL Param \"messageID\" is a unique 32-character alphanumeric identifier assigned by the system, which refers to a specific message within a voicemail box.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, unique 32-character alphanumeric identifier
    voicemail_id = 'voicemail_id_example' # str | Voicemail Box ID, unique 32-character alphanumeric identifier
    message_id = 'message_id_example' # str | Message ID, unique 32-character alphanumeric identifier

    try:
        # Get Voicemail Message File
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get(account_id, voicemail_id, message_id)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, unique 32-character alphanumeric identifier | 
 **voicemail_id** | **str**| Voicemail Box ID, unique 32-character alphanumeric identifier | 
 **message_id** | **str**| Message ID, unique 32-character alphanumeric identifier | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post**
> Dict[str, object] v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post(account_id, voicemail_id, message_id, file)

Add Voicemail Message File

Associate an audio recording file with the voicemail to fully complete the message.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alphanumeric characters
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alphanumeric characters
    message_id = 'message_id_example' # str | Message ID, 32 alphanumeric characters
    file = None # bytearray | Audio file to upload

    try:
        # Add Voicemail Message File
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post(account_id, voicemail_id, message_id, file)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_message_id_raw_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alphanumeric characters | 
 **voicemail_id** | **str**| Voicemail ID, 32 alphanumeric characters | 
 **message_id** | **str**| Message ID, 32 alphanumeric characters | 
 **file** | **bytearray**| Audio file to upload | 

### Return type

**Dict[str, object]**

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

# **v1_account_account_id_voicemail_voicemail_id_message_post**
> ServiceDocsVoicemailMessageGetSingle v1_account_account_id_voicemail_voicemail_id_message_post(account_id, voicemail_id, message)

Create Voicemail Message

Create the container information for a recorded voicemail message in a voicemail box.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_message_get_single import ServiceDocsVoicemailMessageGetSingle
from openapi_client.models.service_voip_voicemail_message_add_data import ServiceVOIPVoicemailMessageAddData
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | account ID, 32 alphanumeric
    voicemail_id = 'voicemail_id_example' # str | voicemail ID, 32 alphanumeric
    message = openapi_client.ServiceVOIPVoicemailMessageAddData() # ServiceVOIPVoicemailMessageAddData | voicemail message payload fields

    try:
        # Create Voicemail Message
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_message_post(account_id, voicemail_id, message)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID, 32 alphanumeric | 
 **voicemail_id** | **str**| voicemail ID, 32 alphanumeric | 
 **message** | [**ServiceVOIPVoicemailMessageAddData**](ServiceVOIPVoicemailMessageAddData.md)| voicemail message payload fields | 

### Return type

[**ServiceDocsVoicemailMessageGetSingle**](ServiceDocsVoicemailMessageGetSingle.md)

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

# **v1_account_account_id_voicemail_voicemail_id_put**
> ServiceDocsVoicemailGetSingle v1_account_account_id_voicemail_voicemail_id_put(account_id, voicemail_id, req_body)

Update Voicemail Box

Update the settings in an individual voicemail box, such as the owner, PIN, etc.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_voicemail_get_single import ServiceDocsVoicemailGetSingle
from openapi_client.models.service_voip_voicemail_add_edit_data import ServiceVOIPVoicemailAddEditData
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
    api_instance = openapi_client.VoicemailApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    voicemail_id = 'voicemail_id_example' # str | Voicemail ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPVoicemailAddEditData() # ServiceVOIPVoicemailAddEditData | payload fields

    try:
        # Update Voicemail Box
        api_response = api_instance.v1_account_account_id_voicemail_voicemail_id_put(account_id, voicemail_id, req_body)
        print("The response of VoicemailApi->v1_account_account_id_voicemail_voicemail_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicemailApi->v1_account_account_id_voicemail_voicemail_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **voicemail_id** | **str**| Voicemail ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPVoicemailAddEditData**](ServiceVOIPVoicemailAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsVoicemailGetSingle**](ServiceDocsVoicemailGetSingle.md)

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

