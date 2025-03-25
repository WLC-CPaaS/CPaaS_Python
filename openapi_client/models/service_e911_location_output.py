# coding: utf-8

"""
    White Label Communications CPaas API Documentation

    A CPaaS platform API

    The version of the OpenAPI document: 1.1
    Contact: support@whitelabelcomm.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.service_e911_legacy_data_output import ServiceE911LegacyDataOutput
from openapi_client.models.service_e911_status_output import ServiceE911StatusOutput
from typing import Optional, Set
from typing_extensions import Self

class ServiceE911LocationOutput(BaseModel):
    """
    ServiceE911LocationOutput
    """ # noqa: E501
    activated_time: Optional[StrictStr] = None
    address_1: Optional[StrictStr] = None
    address_2: Optional[StrictStr] = None
    caller_name: Optional[StrictStr] = None
    comments: Optional[StrictStr] = None
    community: Optional[StrictStr] = None
    customer_order_id: Optional[StrictStr] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    legacy_data: Optional[ServiceE911LegacyDataOutput] = None
    location_id: Optional[StrictStr] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    plus_four: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    status: Optional[ServiceE911StatusOutput] = None
    type: Optional[StrictStr] = None
    update_time: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["activated_time", "address_1", "address_2", "caller_name", "comments", "community", "customer_order_id", "latitude", "legacy_data", "location_id", "longitude", "plus_four", "postal_code", "state", "status", "type", "update_time"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ServiceE911LocationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of legacy_data
        if self.legacy_data:
            _dict['legacy_data'] = self.legacy_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceE911LocationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activated_time": obj.get("activated_time"),
            "address_1": obj.get("address_1"),
            "address_2": obj.get("address_2"),
            "caller_name": obj.get("caller_name"),
            "comments": obj.get("comments"),
            "community": obj.get("community"),
            "customer_order_id": obj.get("customer_order_id"),
            "latitude": obj.get("latitude"),
            "legacy_data": ServiceE911LegacyDataOutput.from_dict(obj["legacy_data"]) if obj.get("legacy_data") is not None else None,
            "location_id": obj.get("location_id"),
            "longitude": obj.get("longitude"),
            "plus_four": obj.get("plus_four"),
            "postal_code": obj.get("postal_code"),
            "state": obj.get("state"),
            "status": ServiceE911StatusOutput.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "type": obj.get("type"),
            "update_time": obj.get("update_time")
        })
        return _obj


