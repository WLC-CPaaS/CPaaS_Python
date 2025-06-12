# openapi_client.CallQueueRecipientApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_loginrecipient_recipient_id_post**](CallQueueRecipientApi.md#v1_account_account_id_loginrecipient_recipient_id_post) | **POST** /v1/account/{accountID}/loginrecipient/{recipientID} | Login as Recipient
[**v1_account_account_id_queuerecipient_get**](CallQueueRecipientApi.md#v1_account_account_id_queuerecipient_get) | **GET** /v1/account/{accountID}/queuerecipient | Change Recipient Status
[**v1_account_account_id_recipient_recipient_id_status_post**](CallQueueRecipientApi.md#v1_account_account_id_recipient_recipient_id_status_post) | **POST** /v1/account/{accountID}/recipient/{recipientID}/status | Get Recipient List


# **v1_account_account_id_loginrecipient_recipient_id_post**
> ServiceDocsCallQueueResponseShort v1_account_account_id_loginrecipient_recipient_id_post(account_id, recipient_id, req_body)

Login as Recipient

Agents must log in to receive calls. Depending on their membership, they can log in to one or more queues. (If an agent is a member of more than one queue, they will receive calls from all the queues they are a part of.)

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_response_short import ServiceDocsCallQueueResponseShort
from openapi_client.models.service_voip_call_queue_recipient_login_logout_data import ServiceVOIPCallQueueRecipientLoginLogoutData
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
    api_instance = openapi_client.CallQueueRecipientApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recipient_id = 'recipient_id_example' # str | Recipient ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueRecipientLoginLogoutData() # ServiceVOIPCallQueueRecipientLoginLogoutData | payload fields

    try:
        # Login as Recipient
        api_response = api_instance.v1_account_account_id_loginrecipient_recipient_id_post(account_id, recipient_id, req_body)
        print("The response of CallQueueRecipientApi->v1_account_account_id_loginrecipient_recipient_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueRecipientApi->v1_account_account_id_loginrecipient_recipient_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recipient_id** | **str**| Recipient ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueRecipientLoginLogoutData**](ServiceVOIPCallQueueRecipientLoginLogoutData.md)| payload fields | 

### Return type

[**ServiceDocsCallQueueResponseShort**](ServiceDocsCallQueueResponseShort.md)

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

# **v1_account_account_id_queuerecipient_get**
> ServiceDocsGetQueueRecipients v1_account_account_id_queuerecipient_get(account_id)

Change Recipient Status

Get a list of all recipients in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_get_queue_recipients import ServiceDocsGetQueueRecipients
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
    api_instance = openapi_client.CallQueueRecipientApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Change Recipient Status
        api_response = api_instance.v1_account_account_id_queuerecipient_get(account_id)
        print("The response of CallQueueRecipientApi->v1_account_account_id_queuerecipient_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueRecipientApi->v1_account_account_id_queuerecipient_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsGetQueueRecipients**](ServiceDocsGetQueueRecipients.md)

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

# **v1_account_account_id_recipient_recipient_id_status_post**
> ServiceAPIResponse v1_account_account_id_recipient_recipient_id_status_post(account_id, recipient_id, req_body)

Get Recipient List

Change the status of a recipient to ready, away, etc.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_call_queue_recipient_status_data import ServiceVOIPCallQueueRecipientStatusData
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
    api_instance = openapi_client.CallQueueRecipientApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recipient_id = 'recipient_id_example' # str | Recipient ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueRecipientStatusData() # ServiceVOIPCallQueueRecipientStatusData | payload fields

    try:
        # Get Recipient List
        api_response = api_instance.v1_account_account_id_recipient_recipient_id_status_post(account_id, recipient_id, req_body)
        print("The response of CallQueueRecipientApi->v1_account_account_id_recipient_recipient_id_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueRecipientApi->v1_account_account_id_recipient_recipient_id_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recipient_id** | **str**| Recipient ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueRecipientStatusData**](ServiceVOIPCallQueueRecipientStatusData.md)| payload fields | 

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

