# openapi_client.WebhookApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_webhook_account_account_id_get**](WebhookApi.md#v1_webhook_account_account_id_get) | **GET** /v1/webhook/account/{accountID} | Get Webhook List
[**v1_webhook_account_account_id_post**](WebhookApi.md#v1_webhook_account_account_id_post) | **POST** /v1/webhook/account/{accountID} | Create Webhook
[**v1_webhook_account_account_id_webhook_id_delete**](WebhookApi.md#v1_webhook_account_account_id_webhook_id_delete) | **DELETE** /v1/webhook/account/{accountID}/{webhookID} | Delete Webhook
[**v1_webhook_account_account_id_webhook_id_get**](WebhookApi.md#v1_webhook_account_account_id_webhook_id_get) | **GET** /v1/webhook/account/{accountID}/{webhookID} | Get Webhook Details
[**v1_webhook_account_account_id_webhook_id_put**](WebhookApi.md#v1_webhook_account_account_id_webhook_id_put) | **PUT** /v1/webhook/account/{accountID}/{webhookID} | Update Webhook


# **v1_webhook_account_account_id_get**
> ServiceDocsWebhookGetAll v1_webhook_account_account_id_get(account_id, page_size=page_size, current_page=current_page)

Get Webhook List

Retrieve the webhook list in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_webhook_get_all import ServiceDocsWebhookGetAll
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
    api_instance = openapi_client.WebhookApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)
    current_page = 56 # int | Current Page (optional)

    try:
        # Get Webhook List
        api_response = api_instance.v1_webhook_account_account_id_get(account_id, page_size=page_size, current_page=current_page)
        print("The response of WebhookApi->v1_webhook_account_account_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->v1_webhook_account_account_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 
 **current_page** | **int**| Current Page | [optional] 

### Return type

[**ServiceDocsWebhookGetAll**](ServiceDocsWebhookGetAll.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhook_account_account_id_post**
> ServiceDocsWebhookGetSingle v1_webhook_account_account_id_post(account_id, body)

Create Webhook

Create a webhook for a specific account ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_webhook_get_single import ServiceDocsWebhookGetSingle
from openapi_client.models.service_webhook_add import ServiceWebhookAdd
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
    api_instance = openapi_client.WebhookApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    body = openapi_client.ServiceWebhookAdd() # ServiceWebhookAdd | Webhook data

    try:
        # Create Webhook
        api_response = api_instance.v1_webhook_account_account_id_post(account_id, body)
        print("The response of WebhookApi->v1_webhook_account_account_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->v1_webhook_account_account_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **body** | [**ServiceWebhookAdd**](ServiceWebhookAdd.md)| Webhook data | 

### Return type

[**ServiceDocsWebhookGetSingle**](ServiceDocsWebhookGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhook_account_account_id_webhook_id_delete**
> ServiceDocsWebhookDelete v1_webhook_account_account_id_webhook_id_delete(account_id, webhook_id)

Delete Webhook

Remove a webhook identified by its ID for a particular account ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_webhook_delete import ServiceDocsWebhookDelete
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
    api_instance = openapi_client.WebhookApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    webhook_id = 56 # int | Webhook ID

    try:
        # Delete Webhook
        api_response = api_instance.v1_webhook_account_account_id_webhook_id_delete(account_id, webhook_id)
        print("The response of WebhookApi->v1_webhook_account_account_id_webhook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->v1_webhook_account_account_id_webhook_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **webhook_id** | **int**| Webhook ID | 

### Return type

[**ServiceDocsWebhookDelete**](ServiceDocsWebhookDelete.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhook_account_account_id_webhook_id_get**
> ServiceDocsWebhookGetSingle v1_webhook_account_account_id_webhook_id_get(account_id, webhook_id)

Get Webhook Details

Access details about a single webhook ID for an individual account ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_webhook_get_single import ServiceDocsWebhookGetSingle
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
    api_instance = openapi_client.WebhookApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    webhook_id = 56 # int | Webhook ID

    try:
        # Get Webhook Details
        api_response = api_instance.v1_webhook_account_account_id_webhook_id_get(account_id, webhook_id)
        print("The response of WebhookApi->v1_webhook_account_account_id_webhook_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->v1_webhook_account_account_id_webhook_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **webhook_id** | **int**| Webhook ID | 

### Return type

[**ServiceDocsWebhookGetSingle**](ServiceDocsWebhookGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhook_account_account_id_webhook_id_put**
> ServiceDocsWebhookGetSingle v1_webhook_account_account_id_webhook_id_put(account_id, webhook_id, body)

Update Webhook

Update a webhook identified by its ID for a distinct account ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_webhook_get_single import ServiceDocsWebhookGetSingle
from openapi_client.models.service_webhook_edit import ServiceWebhookEdit
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
    api_instance = openapi_client.WebhookApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    webhook_id = 'webhook_id_example' # str | Webhook ID
    body = openapi_client.ServiceWebhookEdit() # ServiceWebhookEdit | Updated webhook data

    try:
        # Update Webhook
        api_response = api_instance.v1_webhook_account_account_id_webhook_id_put(account_id, webhook_id, body)
        print("The response of WebhookApi->v1_webhook_account_account_id_webhook_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->v1_webhook_account_account_id_webhook_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **webhook_id** | **str**| Webhook ID | 
 **body** | [**ServiceWebhookEdit**](ServiceWebhookEdit.md)| Updated webhook data | 

### Return type

[**ServiceDocsWebhookGetSingle**](ServiceDocsWebhookGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

