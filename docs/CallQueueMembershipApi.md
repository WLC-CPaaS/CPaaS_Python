# openapi_client.CallQueueMembershipApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_queuemembership_post**](CallQueueMembershipApi.md#v1_account_account_id_queuemembership_post) | **POST** /v1/account/{accountID}/queuemembership | Grant Queue Membership to User
[**v1_account_account_id_queuemembership_recipient_id_disable_post**](CallQueueMembershipApi.md#v1_account_account_id_queuemembership_recipient_id_disable_post) | **POST** /v1/account/{accountID}/queuemembership/{recipientID}/disable | Disable Queue Membership
[**v1_account_account_id_queuemembership_recipient_id_enable_post**](CallQueueMembershipApi.md#v1_account_account_id_queuemembership_recipient_id_enable_post) | **POST** /v1/account/{accountID}/queuemembership/{recipientID}/enable | Enable Queue Membership


# **v1_account_account_id_queuemembership_post**
> ServiceDocsCallQueueMemberGetSingle v1_account_account_id_queuemembership_post(account_id, req_body)

Grant Queue Membership to User

Allow users to create queue memberships for recipients.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_queue_member_get_single import ServiceDocsCallQueueMemberGetSingle
from openapi_client.models.service_voip_queue_membership_add_data import ServiceVOIPQueueMembershipAddData
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
    api_instance = openapi_client.CallQueueMembershipApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPQueueMembershipAddData() # ServiceVOIPQueueMembershipAddData | payload fields

    try:
        # Grant Queue Membership to User
        api_response = api_instance.v1_account_account_id_queuemembership_post(account_id, req_body)
        print("The response of CallQueueMembershipApi->v1_account_account_id_queuemembership_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueMembershipApi->v1_account_account_id_queuemembership_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPQueueMembershipAddData**](ServiceVOIPQueueMembershipAddData.md)| payload fields | 

### Return type

[**ServiceDocsCallQueueMemberGetSingle**](ServiceDocsCallQueueMemberGetSingle.md)

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

# **v1_account_account_id_queuemembership_recipient_id_disable_post**
> ServiceAPIResponse v1_account_account_id_queuemembership_recipient_id_disable_post(account_id, recipient_id)

Disable Queue Membership

Deactivate queue membership for a recipient.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
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
    api_instance = openapi_client.CallQueueMembershipApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recipient_id = 'recipient_id_example' # str | Recipient ID, 32 alpha numeric

    try:
        # Disable Queue Membership
        api_response = api_instance.v1_account_account_id_queuemembership_recipient_id_disable_post(account_id, recipient_id)
        print("The response of CallQueueMembershipApi->v1_account_account_id_queuemembership_recipient_id_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueMembershipApi->v1_account_account_id_queuemembership_recipient_id_disable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recipient_id** | **str**| Recipient ID, 32 alpha numeric | 

### Return type

[**ServiceAPIResponse**](ServiceAPIResponse.md)

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

# **v1_account_account_id_queuemembership_recipient_id_enable_post**
> ServiceAPIResponse v1_account_account_id_queuemembership_recipient_id_enable_post(account_id, recipient_id, req_body)

Enable Queue Membership

Activate queue membership for a recipient.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_call_queue_enable_membership_data import ServiceVOIPCallQueueEnableMembershipData
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
    api_instance = openapi_client.CallQueueMembershipApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recipient_id = 'recipient_id_example' # str | Recipient ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPCallQueueEnableMembershipData() # ServiceVOIPCallQueueEnableMembershipData | payload fields

    try:
        # Enable Queue Membership
        api_response = api_instance.v1_account_account_id_queuemembership_recipient_id_enable_post(account_id, recipient_id, req_body)
        print("The response of CallQueueMembershipApi->v1_account_account_id_queuemembership_recipient_id_enable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallQueueMembershipApi->v1_account_account_id_queuemembership_recipient_id_enable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recipient_id** | **str**| Recipient ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPCallQueueEnableMembershipData**](ServiceVOIPCallQueueEnableMembershipData.md)| payload fields | 

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

