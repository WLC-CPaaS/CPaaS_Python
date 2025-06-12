# openapi_client.SMSApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_sms_account_account_id_campaign_campaign_id_import_get**](SMSApi.md#v1_sms_account_account_id_campaign_campaign_id_import_get) | **GET** /v1/sms/account/{accountID}/campaign/{campaignID}/import | 
[**v1_sms_account_account_id_campaign_campaign_id_import_post**](SMSApi.md#v1_sms_account_account_id_campaign_campaign_id_import_post) | **POST** /v1/sms/account/{accountID}/campaign/{campaignID}/import | 
[**v1_sms_account_account_id_campaign_campaign_id_phonenumber_get**](SMSApi.md#v1_sms_account_account_id_campaign_campaign_id_phonenumber_get) | **GET** /v1/sms/account/{accountID}/campaign/{campaignID}/phonenumber | 
[**v1_sms_account_account_id_campaign_campaign_id_phonenumber_put**](SMSApi.md#v1_sms_account_account_id_campaign_campaign_id_phonenumber_put) | **PUT** /v1/sms/account/{accountID}/campaign/{campaignID}/phonenumber | 
[**v1_sms_account_account_id_campaign_import_get**](SMSApi.md#v1_sms_account_account_id_campaign_import_get) | **GET** /v1/sms/account/{accountID}/campaign/import | 


# **v1_sms_account_account_id_campaign_campaign_id_import_get**
> ServiceDocsCampaignImportOutput v1_sms_account_account_id_campaign_campaign_id_import_get(account_id, campaign_id)

Get details about a single imported campaign in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_campaign_import_output import ServiceDocsCampaignImportOutput
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
    api_instance = openapi_client.SMSApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    campaign_id = 'campaign_id_example' # str | Campaign ID

    try:
        api_response = api_instance.v1_sms_account_account_id_campaign_campaign_id_import_get(account_id, campaign_id)
        print("The response of SMSApi->v1_sms_account_account_id_campaign_campaign_id_import_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->v1_sms_account_account_id_campaign_campaign_id_import_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **campaign_id** | **str**| Campaign ID | 

### Return type

[**ServiceDocsCampaignImportOutput**](ServiceDocsCampaignImportOutput.md)

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

# **v1_sms_account_account_id_campaign_campaign_id_import_post**
> ServiceDocsCampaignImportOutput v1_sms_account_account_id_campaign_campaign_id_import_post(account_id, campaign_id)

Import campaign

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_campaign_import_output import ServiceDocsCampaignImportOutput
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
    api_instance = openapi_client.SMSApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    campaign_id = 'campaign_id_example' # str | Campaign ID

    try:
        api_response = api_instance.v1_sms_account_account_id_campaign_campaign_id_import_post(account_id, campaign_id)
        print("The response of SMSApi->v1_sms_account_account_id_campaign_campaign_id_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->v1_sms_account_account_id_campaign_campaign_id_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **campaign_id** | **str**| Campaign ID | 

### Return type

[**ServiceDocsCampaignImportOutput**](ServiceDocsCampaignImportOutput.md)

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

# **v1_sms_account_account_id_campaign_campaign_id_phonenumber_get**
> ServiceDocsCampaignPhoneNumberOutput v1_sms_account_account_id_campaign_campaign_id_phonenumber_get(account_id, campaign_id, page_num=page_num, page_size=page_size)

Get telephone numbers associated with a campaign.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_campaign_phone_number_output import ServiceDocsCampaignPhoneNumberOutput
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
    api_instance = openapi_client.SMSApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    campaign_id = 'campaign_id_example' # str | Campaign ID
    page_num = 3.4 # float | Page number (optional)
    page_size = 3.4 # float | Page size (optional)

    try:
        api_response = api_instance.v1_sms_account_account_id_campaign_campaign_id_phonenumber_get(account_id, campaign_id, page_num=page_num, page_size=page_size)
        print("The response of SMSApi->v1_sms_account_account_id_campaign_campaign_id_phonenumber_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->v1_sms_account_account_id_campaign_campaign_id_phonenumber_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **campaign_id** | **str**| Campaign ID | 
 **page_num** | **float**| Page number | [optional] 
 **page_size** | **float**| Page size | [optional] 

### Return type

[**ServiceDocsCampaignPhoneNumberOutput**](ServiceDocsCampaignPhoneNumberOutput.md)

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

# **v1_sms_account_account_id_campaign_campaign_id_phonenumber_put**
> ServiceDocsCampaignTagDetagPhonenumbersOutput v1_sms_account_account_id_campaign_campaign_id_phonenumber_put(account_id, campaign_id, req_body)

Associate or dissociate telephone numbers with a campaign.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_campaign_tag_detag_phonenumbers import ServiceCampaignTagDetagPhonenumbers
from openapi_client.models.service_docs_campaign_tag_detag_phonenumbers_output import ServiceDocsCampaignTagDetagPhonenumbersOutput
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
    api_instance = openapi_client.SMSApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    campaign_id = 'campaign_id_example' # str | Campaign ID, 32 alpha numeric
    req_body = openapi_client.ServiceCampaignTagDetagPhonenumbers() # ServiceCampaignTagDetagPhonenumbers | payload fields

    try:
        api_response = api_instance.v1_sms_account_account_id_campaign_campaign_id_phonenumber_put(account_id, campaign_id, req_body)
        print("The response of SMSApi->v1_sms_account_account_id_campaign_campaign_id_phonenumber_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->v1_sms_account_account_id_campaign_campaign_id_phonenumber_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **campaign_id** | **str**| Campaign ID, 32 alpha numeric | 
 **req_body** | [**ServiceCampaignTagDetagPhonenumbers**](ServiceCampaignTagDetagPhonenumbers.md)| payload fields | 

### Return type

[**ServiceDocsCampaignTagDetagPhonenumbersOutput**](ServiceDocsCampaignTagDetagPhonenumbersOutput.md)

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

# **v1_sms_account_account_id_campaign_import_get**
> ServiceDocsCampaignImportedGetAllOutput v1_sms_account_account_id_campaign_import_get(account_id, page_num=page_num, page_size=page_size)

Get a list of all imported campaigns in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_campaign_imported_get_all_output import ServiceDocsCampaignImportedGetAllOutput
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
    api_instance = openapi_client.SMSApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    page_num = 3.4 # float | Page number (optional)
    page_size = 3.4 # float | Page size (optional)

    try:
        api_response = api_instance.v1_sms_account_account_id_campaign_import_get(account_id, page_num=page_num, page_size=page_size)
        print("The response of SMSApi->v1_sms_account_account_id_campaign_import_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->v1_sms_account_account_id_campaign_import_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **page_num** | **float**| Page number | [optional] 
 **page_size** | **float**| Page size | [optional] 

### Return type

[**ServiceDocsCampaignImportedGetAllOutput**](ServiceDocsCampaignImportedGetAllOutput.md)

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

