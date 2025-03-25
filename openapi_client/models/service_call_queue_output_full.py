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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ServiceCallQueueOutputFull(BaseModel):
    """
    ServiceCallQueueOutputFull
    """ # noqa: E501
    agent_wrapup_time: Optional[StrictInt] = None
    features: Optional[Dict[str, Any]] = None
    force_away_on_reject: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    queue_router: Optional[StrictStr] = None
    queue_type: Optional[StrictStr] = None
    ring_timeout: Optional[StrictInt] = None
    tick_time: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["agent_wrapup_time", "features", "force_away_on_reject", "id", "name", "queue_router", "queue_type", "ring_timeout", "tick_time"]

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
        """Create an instance of ServiceCallQueueOutputFull from a JSON string"""
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
        """Create an instance of ServiceCallQueueOutputFull from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_wrapup_time": obj.get("agent_wrapup_time"),
            "features": obj.get("features"),
            "force_away_on_reject": obj.get("force_away_on_reject"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "queue_router": obj.get("queue_router"),
            "queue_type": obj.get("queue_type"),
            "ring_timeout": obj.get("ring_timeout"),
            "tick_time": obj.get("tick_time")
        })
        return _obj


