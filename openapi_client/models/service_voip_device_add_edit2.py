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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.service_call_forward import ServiceCallForward
from openapi_client.models.service_call_recording_settings import ServiceCallRecordingSettings
from openapi_client.models.service_music_on_hold import ServiceMusicOnHold
from openapi_client.models.service_voip_device_add_edit3a import ServiceVOIPDeviceAddEdit3a
from openapi_client.models.service_voip_device_add_edit3c import ServiceVOIPDeviceAddEdit3c
from openapi_client.models.service_voip_shared_do_not_disturb import ServiceVOIPSharedDoNotDisturb
from typing import Optional, Set
from typing_extensions import Self

class ServiceVOIPDeviceAddEdit2(BaseModel):
    """
    ServiceVOIPDeviceAddEdit2
    """ # noqa: E501
    call_forward: Optional[ServiceCallForward] = None
    call_recording: Optional[ServiceCallRecordingSettings] = None
    caller_id: Optional[ServiceVOIPDeviceAddEdit3c] = None
    device_type: Optional[StrictStr] = None
    do_not_disturb: Optional[ServiceVOIPSharedDoNotDisturb] = None
    enabled: Optional[StrictBool] = Field(default=None, description="cannot use required, else it has to be true and false is not allowed")
    mac_address: Optional[StrictStr] = Field(default=None, description="dont use mac, it enforces :, which voip does not like")
    music_on_hold: Optional[ServiceMusicOnHold] = None
    name: Annotated[str, Field(strict=True, max_length=128)]
    owner_id: Optional[StrictStr] = Field(default=None, description="json omitempty is needed else voip fails on \"\" for owner_id")
    sip: ServiceVOIPDeviceAddEdit3a
    __properties: ClassVar[List[str]] = ["call_forward", "call_recording", "caller_id", "device_type", "do_not_disturb", "enabled", "mac_address", "music_on_hold", "name", "owner_id", "sip"]

    @field_validator('device_type')
    def device_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['softphone', 'sip_uri']):
            raise ValueError("must be one of enum values ('softphone', 'sip_uri')")
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
        """Create an instance of ServiceVOIPDeviceAddEdit2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of call_forward
        if self.call_forward:
            _dict['call_forward'] = self.call_forward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of call_recording
        if self.call_recording:
            _dict['call_recording'] = self.call_recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of caller_id
        if self.caller_id:
            _dict['caller_id'] = self.caller_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of do_not_disturb
        if self.do_not_disturb:
            _dict['do_not_disturb'] = self.do_not_disturb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of music_on_hold
        if self.music_on_hold:
            _dict['music_on_hold'] = self.music_on_hold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sip
        if self.sip:
            _dict['sip'] = self.sip.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceVOIPDeviceAddEdit2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "call_forward": ServiceCallForward.from_dict(obj["call_forward"]) if obj.get("call_forward") is not None else None,
            "call_recording": ServiceCallRecordingSettings.from_dict(obj["call_recording"]) if obj.get("call_recording") is not None else None,
            "caller_id": ServiceVOIPDeviceAddEdit3c.from_dict(obj["caller_id"]) if obj.get("caller_id") is not None else None,
            "device_type": obj.get("device_type"),
            "do_not_disturb": ServiceVOIPSharedDoNotDisturb.from_dict(obj["do_not_disturb"]) if obj.get("do_not_disturb") is not None else None,
            "enabled": obj.get("enabled"),
            "mac_address": obj.get("mac_address"),
            "music_on_hold": ServiceMusicOnHold.from_dict(obj["music_on_hold"]) if obj.get("music_on_hold") is not None else None,
            "name": obj.get("name"),
            "owner_id": obj.get("owner_id"),
            "sip": ServiceVOIPDeviceAddEdit3a.from_dict(obj["sip"]) if obj.get("sip") is not None else None
        })
        return _obj


