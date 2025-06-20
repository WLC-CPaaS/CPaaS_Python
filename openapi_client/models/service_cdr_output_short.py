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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ServiceCdrOutputShort(BaseModel):
    """
    ServiceCdrOutputShort
    """ # noqa: E501
    authorizing_id: Optional[StrictStr] = None
    billing_seconds: Optional[StrictInt] = None
    bridge_id: Optional[StrictStr] = None
    call_id: Optional[StrictStr] = None
    call_priority: Optional[StrictStr] = None
    call_type: Optional[StrictStr] = None
    callee_id_name: Optional[StrictStr] = None
    callee_id_number: Optional[StrictStr] = None
    caller_id_name: Optional[StrictStr] = None
    caller_id_number: Optional[StrictStr] = None
    calling_from: Optional[StrictStr] = None
    cost: Optional[StrictStr] = None
    dialed_number: Optional[StrictStr] = None
    direction: Optional[StrictStr] = None
    duration_seconds: Optional[StrictInt] = None
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    hangup_cause: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    interaction_id: Optional[StrictStr] = None
    media_recordings: Optional[List[Dict[str, Any]]] = None
    media_server: Optional[StrictStr] = None
    other_leg_call_id: Optional[StrictStr] = None
    owner_id: Optional[StrictStr] = None
    rate: Optional[StrictStr] = None
    rate_name: Optional[StrictStr] = None
    recording_url: Optional[StrictStr] = None
    request: Optional[StrictStr] = None
    timestamp: Optional[StrictInt] = None
    timestamp_datetime: Optional[StrictStr] = None
    to: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["authorizing_id", "billing_seconds", "bridge_id", "call_id", "call_priority", "call_type", "callee_id_name", "callee_id_number", "caller_id_name", "caller_id_number", "calling_from", "cost", "dialed_number", "direction", "duration_seconds", "from", "hangup_cause", "id", "interaction_id", "media_recordings", "media_server", "other_leg_call_id", "owner_id", "rate", "rate_name", "recording_url", "request", "timestamp", "timestamp_datetime", "to"]

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
        """Create an instance of ServiceCdrOutputShort from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceCdrOutputShort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorizing_id": obj.get("authorizing_id"),
            "billing_seconds": obj.get("billing_seconds"),
            "bridge_id": obj.get("bridge_id"),
            "call_id": obj.get("call_id"),
            "call_priority": obj.get("call_priority"),
            "call_type": obj.get("call_type"),
            "callee_id_name": obj.get("callee_id_name"),
            "callee_id_number": obj.get("callee_id_number"),
            "caller_id_name": obj.get("caller_id_name"),
            "caller_id_number": obj.get("caller_id_number"),
            "calling_from": obj.get("calling_from"),
            "cost": obj.get("cost"),
            "dialed_number": obj.get("dialed_number"),
            "direction": obj.get("direction"),
            "duration_seconds": obj.get("duration_seconds"),
            "from": obj.get("from"),
            "hangup_cause": obj.get("hangup_cause"),
            "id": obj.get("id"),
            "interaction_id": obj.get("interaction_id"),
            "media_recordings": obj.get("media_recordings"),
            "media_server": obj.get("media_server"),
            "other_leg_call_id": obj.get("other_leg_call_id"),
            "owner_id": obj.get("owner_id"),
            "rate": obj.get("rate"),
            "rate_name": obj.get("rate_name"),
            "recording_url": obj.get("recording_url"),
            "request": obj.get("request"),
            "timestamp": obj.get("timestamp"),
            "timestamp_datetime": obj.get("timestamp_datetime"),
            "to": obj.get("to")
        })
        return _obj


