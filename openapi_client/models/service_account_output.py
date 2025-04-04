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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.service_voip_account_call_recording import ServiceVOIPAccountCallRecording
from openapi_client.models.service_voip_account_music_on_hold import ServiceVOIPAccountMusicOnHold
from openapi_client.models.service_voip_shared_do_not_disturb import ServiceVOIPSharedDoNotDisturb
from typing import Optional, Set
from typing_extensions import Self

class ServiceAccountOutput(BaseModel):
    """
    ServiceAccountOutput
    """ # noqa: E501
    call_recording: Optional[ServiceVOIPAccountCallRecording] = None
    do_not_disturb: Optional[ServiceVOIPSharedDoNotDisturb] = None
    enabled: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    music_on_hold: Optional[ServiceVOIPAccountMusicOnHold] = None
    name: Optional[StrictStr] = None
    realm: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["call_recording", "do_not_disturb", "enabled", "id", "music_on_hold", "name", "realm", "timezone"]

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
        """Create an instance of ServiceAccountOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of call_recording
        if self.call_recording:
            _dict['call_recording'] = self.call_recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of do_not_disturb
        if self.do_not_disturb:
            _dict['do_not_disturb'] = self.do_not_disturb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of music_on_hold
        if self.music_on_hold:
            _dict['music_on_hold'] = self.music_on_hold.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceAccountOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "call_recording": ServiceVOIPAccountCallRecording.from_dict(obj["call_recording"]) if obj.get("call_recording") is not None else None,
            "do_not_disturb": ServiceVOIPSharedDoNotDisturb.from_dict(obj["do_not_disturb"]) if obj.get("do_not_disturb") is not None else None,
            "enabled": obj.get("enabled"),
            "id": obj.get("id"),
            "music_on_hold": ServiceVOIPAccountMusicOnHold.from_dict(obj["music_on_hold"]) if obj.get("music_on_hold") is not None else None,
            "name": obj.get("name"),
            "realm": obj.get("realm"),
            "timezone": obj.get("timezone")
        })
        return _obj


