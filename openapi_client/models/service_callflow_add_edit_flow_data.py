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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ServiceCallflowAddEditFlowData(BaseModel):
    """
    ServiceCallflowAddEditFlowData
    """ # noqa: E501
    children: Optional[Dict[str, ServiceCallflowAddEditFlowData]] = None
    data: Optional[Dict[str, Any]] = None
    module: StrictStr
    __properties: ClassVar[List[str]] = ["children", "data", "module"]

    @field_validator('module')
    def module_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['device', 'offnet', 'menu', 'play', 'temporal_route', 'voicemail', 'user', 'call_forward', 'group', 'ring_group', 'do_not_disturb', 'park', 'group_pickup', 'group_pickup_feature', 'intercom', 'page_group', 'record_call', 'record_caller', 'qubicle', 'missed_call_alert']):
            raise ValueError("must be one of enum values ('device', 'offnet', 'menu', 'play', 'temporal_route', 'voicemail', 'user', 'call_forward', 'group', 'ring_group', 'do_not_disturb', 'park', 'group_pickup', 'group_pickup_feature', 'intercom', 'page_group', 'record_call', 'record_caller', 'qubicle', 'missed_call_alert')")
        return value

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
        """Create an instance of ServiceCallflowAddEditFlowData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in children (dict)
        _field_dict = {}
        if self.children:
            for _key_children in self.children:
                if self.children[_key_children]:
                    _field_dict[_key_children] = self.children[_key_children].to_dict()
            _dict['children'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceCallflowAddEditFlowData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "children": dict(
                (_k, ServiceCallflowAddEditFlowData.from_dict(_v))
                for _k, _v in obj["children"].items()
            )
            if obj.get("children") is not None
            else None,
            "data": obj.get("data"),
            "module": obj.get("module")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
ServiceCallflowAddEditFlowData.model_rebuild(raise_errors=False)

