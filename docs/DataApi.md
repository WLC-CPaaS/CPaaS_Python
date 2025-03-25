# openapi_client.DataApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_data_call_daily_summary_get**](DataApi.md#v1_data_call_daily_summary_get) | **GET** /v1/data/call_daily_summary | Get Call Daily Summary List
[**v1_data_call_detail_get**](DataApi.md#v1_data_call_detail_get) | **GET** /v1/data/call_detail | Get Call Detail List
[**v1_data_call_monthly_summary_get**](DataApi.md#v1_data_call_monthly_summary_get) | **GET** /v1/data/call_monthly_summary | Get Call Detail List
[**v1_data_endpoint_list_get**](DataApi.md#v1_data_endpoint_list_get) | **GET** /v1/data/endpoint_list | Get Endpoint List
[**v1_data_event_daily_summary_get**](DataApi.md#v1_data_event_daily_summary_get) | **GET** /v1/data/event_daily_summary | Get Event Daily Summary List
[**v1_data_event_detail_get**](DataApi.md#v1_data_event_detail_get) | **GET** /v1/data/event_detail | Get Event Details
[**v1_data_event_monthly_summary_get**](DataApi.md#v1_data_event_monthly_summary_get) | **GET** /v1/data/event_monthly_summary | Get Event Monthly Summary List
[**v1_data_feature_daily_summary_get**](DataApi.md#v1_data_feature_daily_summary_get) | **GET** /v1/data/feature_daily_summary | Get Feature Daily Summary List
[**v1_data_feature_monthly_summary_get**](DataApi.md#v1_data_feature_monthly_summary_get) | **GET** /v1/data/feature_monthly_summary | Get Feature Monthly Summary List


# **v1_data_call_daily_summary_get**
> ServiceDocsCallDailySummary v1_data_call_daily_summary_get(account_id=account_id, call_type=call_type, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)

Get Call Daily Summary List

Retrieve a paginated list of call daily summary based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_daily_summary import ServiceDocsCallDailySummary
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
    api_instance = openapi_client.DataApi(api_client)
    account_id = 'account_id_example' # str |  (optional)
    call_type = 'call_type_example' # str |  (optional)
    end_date = 'end_date_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_date = 'start_date_example' # str |  (optional)
    start_key = 'start_key_example' # str |  (optional)

    try:
        # Get Call Daily Summary List
        api_response = api_instance.v1_data_call_daily_summary_get(account_id=account_id, call_type=call_type, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)
        print("The response of DataApi->v1_data_call_daily_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_call_daily_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **call_type** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **start_key** | **str**|  | [optional] 

### Return type

[**ServiceDocsCallDailySummary**](ServiceDocsCallDailySummary.md)

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

# **v1_data_call_detail_get**
> ServiceDocsCallDetail v1_data_call_detail_get(account=account, call_type=call_type, callee_name=callee_name, callee_number=callee_number, caller_name=caller_name, caller_number=caller_number, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)

Get Call Detail List

Retrieve a paginated list of call details based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_detail import ServiceDocsCallDetail
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
    api_instance = openapi_client.DataApi(api_client)
    account = 'account_example' # str |  (optional)
    call_type = 'call_type_example' # str |  (optional)
    callee_name = 'callee_name_example' # str |  (optional)
    callee_number = 'callee_number_example' # str |  (optional)
    caller_name = 'caller_name_example' # str |  (optional)
    caller_number = 'caller_number_example' # str |  (optional)
    end_date = 'end_date_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_date = 'start_date_example' # str |  (optional)
    start_key = 'start_key_example' # str |  (optional)

    try:
        # Get Call Detail List
        api_response = api_instance.v1_data_call_detail_get(account=account, call_type=call_type, callee_name=callee_name, callee_number=callee_number, caller_name=caller_name, caller_number=caller_number, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)
        print("The response of DataApi->v1_data_call_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_call_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 
 **call_type** | **str**|  | [optional] 
 **callee_name** | **str**|  | [optional] 
 **callee_number** | **str**|  | [optional] 
 **caller_name** | **str**|  | [optional] 
 **caller_number** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **start_key** | **str**|  | [optional] 

### Return type

[**ServiceDocsCallDetail**](ServiceDocsCallDetail.md)

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

# **v1_data_call_monthly_summary_get**
> ServiceDocsCallMonthlySummary v1_data_call_monthly_summary_get(account=account, call_type=call_type, end_month=end_month, end_year=end_year, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)

Get Call Detail List

Retrieve a paginated list of call monthly summary based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_monthly_summary import ServiceDocsCallMonthlySummary
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
    api_instance = openapi_client.DataApi(api_client)
    account = 'account_example' # str |  (optional)
    call_type = 'call_type_example' # str |  (optional)
    end_month = 56 # int |  (optional)
    end_year = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    start_month = 56 # int |  (optional)
    start_year = 56 # int |  (optional)

    try:
        # Get Call Detail List
        api_response = api_instance.v1_data_call_monthly_summary_get(account=account, call_type=call_type, end_month=end_month, end_year=end_year, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)
        print("The response of DataApi->v1_data_call_monthly_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_call_monthly_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 
 **call_type** | **str**|  | [optional] 
 **end_month** | **int**|  | [optional] 
 **end_year** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **start_month** | **int**|  | [optional] 
 **start_year** | **int**|  | [optional] 

### Return type

[**ServiceDocsCallMonthlySummary**](ServiceDocsCallMonthlySummary.md)

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

# **v1_data_endpoint_list_get**
> ServiceDocsEndpointList v1_data_endpoint_list_get(endpoint_name=endpoint_name, feature_name=feature_name, page_size=page_size, start_key=start_key, transaction_type=transaction_type, version=version)

Get Endpoint List

Retrieve a paginated list of endpoints based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_endpoint_list import ServiceDocsEndpointList
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
    api_instance = openapi_client.DataApi(api_client)
    endpoint_name = 'endpoint_name_example' # str |  (optional)
    feature_name = 'feature_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    transaction_type = 'transaction_type_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Get Endpoint List
        api_response = api_instance.v1_data_endpoint_list_get(endpoint_name=endpoint_name, feature_name=feature_name, page_size=page_size, start_key=start_key, transaction_type=transaction_type, version=version)
        print("The response of DataApi->v1_data_endpoint_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_endpoint_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**|  | [optional] 
 **feature_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **transaction_type** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**ServiceDocsEndpointList**](ServiceDocsEndpointList.md)

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

# **v1_data_event_daily_summary_get**
> ServiceDocsEventDailySummary v1_data_event_daily_summary_get(account_id=account_id, component=component, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)

Get Event Daily Summary List

Retrieve a paginated list of event daily summaries based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_event_daily_summary import ServiceDocsEventDailySummary
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
    api_instance = openapi_client.DataApi(api_client)
    account_id = 'account_id_example' # str |  (optional)
    component = 'component_example' # str |  (optional)
    end_date = 'end_date_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_date = 'start_date_example' # str |  (optional)
    start_key = 'start_key_example' # str |  (optional)

    try:
        # Get Event Daily Summary List
        api_response = api_instance.v1_data_event_daily_summary_get(account_id=account_id, component=component, end_date=end_date, page_size=page_size, start_date=start_date, start_key=start_key)
        print("The response of DataApi->v1_data_event_daily_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_event_daily_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **component** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **start_key** | **str**|  | [optional] 

### Return type

[**ServiceDocsEventDailySummary**](ServiceDocsEventDailySummary.md)

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

# **v1_data_event_detail_get**
> ServiceDocsEventDetail v1_data_event_detail_get(account_id=account_id, component=component, end_date_time=end_date_time, event_name=event_name, exec_status=exec_status, page_size=page_size, start_date_time=start_date_time, start_key=start_key, username=username)

Get Event Details

Retrieve a paginated list of event detail based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_event_detail import ServiceDocsEventDetail
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
    api_instance = openapi_client.DataApi(api_client)
    account_id = 'account_id_example' # str |  (optional)
    component = 'component_example' # str |  (optional)
    end_date_time = 'end_date_time_example' # str |  (optional)
    event_name = 'event_name_example' # str |  (optional)
    exec_status = 'exec_status_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_date_time = 'start_date_time_example' # str |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        # Get Event Details
        api_response = api_instance.v1_data_event_detail_get(account_id=account_id, component=component, end_date_time=end_date_time, event_name=event_name, exec_status=exec_status, page_size=page_size, start_date_time=start_date_time, start_key=start_key, username=username)
        print("The response of DataApi->v1_data_event_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_event_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **component** | **str**|  | [optional] 
 **end_date_time** | **str**|  | [optional] 
 **event_name** | **str**|  | [optional] 
 **exec_status** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_date_time** | **str**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**ServiceDocsEventDetail**](ServiceDocsEventDetail.md)

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

# **v1_data_event_monthly_summary_get**
> ServiceDocsEventMonthlySummary v1_data_event_monthly_summary_get(account_id=account_id, component=component, end_month=end_month, end_year=end_year, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)

Get Event Monthly Summary List

Retrieve a paginated list of event monthly summaries based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_event_monthly_summary import ServiceDocsEventMonthlySummary
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
    api_instance = openapi_client.DataApi(api_client)
    account_id = 'account_id_example' # str |  (optional)
    component = 'component_example' # str |  (optional)
    end_month = 56 # int |  (optional)
    end_year = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    start_month = 56 # int |  (optional)
    start_year = 56 # int |  (optional)

    try:
        # Get Event Monthly Summary List
        api_response = api_instance.v1_data_event_monthly_summary_get(account_id=account_id, component=component, end_month=end_month, end_year=end_year, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)
        print("The response of DataApi->v1_data_event_monthly_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_event_monthly_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **component** | **str**|  | [optional] 
 **end_month** | **int**|  | [optional] 
 **end_year** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **start_month** | **int**|  | [optional] 
 **start_year** | **int**|  | [optional] 

### Return type

[**ServiceDocsEventMonthlySummary**](ServiceDocsEventMonthlySummary.md)

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

# **v1_data_feature_daily_summary_get**
> ServiceDocsFeatureDailySummary v1_data_feature_daily_summary_get(end_date=end_date, feature_name=feature_name, page_size=page_size, start_date=start_date, start_key=start_key)

Get Feature Daily Summary List

Retrieve a paginated list of feature daily summary based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_feature_daily_summary import ServiceDocsFeatureDailySummary
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
    api_instance = openapi_client.DataApi(api_client)
    end_date = 'end_date_example' # str |  (optional)
    feature_name = 'feature_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_date = 'start_date_example' # str |  (optional)
    start_key = 'start_key_example' # str |  (optional)

    try:
        # Get Feature Daily Summary List
        api_response = api_instance.v1_data_feature_daily_summary_get(end_date=end_date, feature_name=feature_name, page_size=page_size, start_date=start_date, start_key=start_key)
        print("The response of DataApi->v1_data_feature_daily_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_feature_daily_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**|  | [optional] 
 **feature_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **start_key** | **str**|  | [optional] 

### Return type

[**ServiceDocsFeatureDailySummary**](ServiceDocsFeatureDailySummary.md)

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

# **v1_data_feature_monthly_summary_get**
> ServiceDocsFeatureMonthlySummary v1_data_feature_monthly_summary_get(end_month=end_month, end_year=end_year, feature_name=feature_name, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)

Get Feature Monthly Summary List

Retrieve a paginated list of feature monthly summary based on query parameters.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_feature_monthly_summary import ServiceDocsFeatureMonthlySummary
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
    api_instance = openapi_client.DataApi(api_client)
    end_month = 56 # int |  (optional)
    end_year = 56 # int |  (optional)
    feature_name = 'feature_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    start_month = 56 # int |  (optional)
    start_year = 56 # int |  (optional)

    try:
        # Get Feature Monthly Summary List
        api_response = api_instance.v1_data_feature_monthly_summary_get(end_month=end_month, end_year=end_year, feature_name=feature_name, page_size=page_size, start_key=start_key, start_month=start_month, start_year=start_year)
        print("The response of DataApi->v1_data_feature_monthly_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->v1_data_feature_monthly_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_month** | **int**|  | [optional] 
 **end_year** | **int**|  | [optional] 
 **feature_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **start_month** | **int**|  | [optional] 
 **start_year** | **int**|  | [optional] 

### Return type

[**ServiceDocsFeatureMonthlySummary**](ServiceDocsFeatureMonthlySummary.md)

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

