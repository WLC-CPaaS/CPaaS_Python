# ServiceParkingSlotData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attended** | **bool** |  | [optional] 
**call_id** | **str** |  | [optional] 
**cid_name** | **str** |  | [optional] 
**cid_number** | **str** |  | [optional] 
**cid_uri** | **str** |  | [optional] 
**from_tag** | **str** |  | [optional] 
**node** | **str** |  | [optional] 
**presence_id** | **str** |  | [optional] 
**presence_realm** | **str** |  | [optional] 
**presence_type** | **str** |  | [optional] 
**presence_user** | **str** |  | [optional] 
**ringback_id** | **str** |  | [optional] 
**slot_call_id** | **str** |  | [optional] 
**switch_uri** | **str** |  | [optional] 
**to_tag** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_parking_slot_data import ServiceParkingSlotData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceParkingSlotData from a JSON string
service_parking_slot_data_instance = ServiceParkingSlotData.from_json(json)
# print the JSON string representation of the object
print(ServiceParkingSlotData.to_json())

# convert the object into a dict
service_parking_slot_data_dict = service_parking_slot_data_instance.to_dict()
# create an instance of ServiceParkingSlotData from a dict
service_parking_slot_data_from_dict = ServiceParkingSlotData.from_dict(service_parking_slot_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


