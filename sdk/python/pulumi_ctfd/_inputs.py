# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ChallengeFileArgs',
    'ChallengeFlagArgs',
    'ChallengeHintArgs',
    'ChallengeRequirementsArgs',
]

@pulumi.input_type
class ChallengeFileArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 content: Optional[pulumi.Input[str]] = None,
                 contentb64: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: Name of the file as displayed to end-users.
        :param pulumi.Input[str] content: Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
        :param pulumi.Input[str] contentb64: Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        :param pulumi.Input[str] id: Identifier of the file, used internally to handle the CTFd corresponding object.
        :param pulumi.Input[str] location: Location where the file is stored on the CTFd instance, for download purposes.
        """
        pulumi.set(__self__, "name", name)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if contentb64 is not None:
            pulumi.set(__self__, "contentb64", contentb64)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the file as displayed to end-users.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        Raw content of the file, perfectly fit the use-cases of a .txt document or anything with a simple binary content. You could provide it from the file-system using `file("${path.module}/...")`.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def contentb64(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 content of the file, perfectly fit the use-cases of complex binaries. You could provide it from the file-system using `filebase64("${path.module}/...")`.
        """
        return pulumi.get(self, "contentb64")

    @contentb64.setter
    def contentb64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contentb64", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the file, used internally to handle the CTFd corresponding object.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location where the file is stored on the CTFd instance, for download purposes.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)


@pulumi.input_type
class ChallengeFlagArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 data: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] content: The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        :param pulumi.Input[str] data: The flag sensitivity information, either case*sensitive or case*insensitive
        :param pulumi.Input[str] id: Identifier of the flag, used internally to handle the CTFd corresponding object.
        :param pulumi.Input[str] type: The type of the flag, could be either static or regex
        """
        pulumi.set(__self__, "content", content)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The actual flag to match. Consider using the convention `MYCTF{value}` with `MYCTF` being the shortcode of your event's name and `value` depending on each challenge.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        The flag sensitivity information, either case*sensitive or case*insensitive
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the flag, used internally to handle the CTFd corresponding object.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the flag, could be either static or regex
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ChallengeHintArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 cost: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 requirements: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] content: Content of the hint as displayed to the end-user.
        :param pulumi.Input[int] cost: Cost of the hint, and if any specified, the end-user will consume its own (or team) points to get it.
        :param pulumi.Input[str] id: Identifier of the hint, used internally to handle the CTFd corresponding object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] requirements: Other hints required to be consumed before getting this one. Useful for cost-increasing hint strategies with more and more help.
        """
        pulumi.set(__self__, "content", content)
        if cost is not None:
            pulumi.set(__self__, "cost", cost)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if requirements is not None:
            pulumi.set(__self__, "requirements", requirements)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Content of the hint as displayed to the end-user.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def cost(self) -> Optional[pulumi.Input[int]]:
        """
        Cost of the hint, and if any specified, the end-user will consume its own (or team) points to get it.
        """
        return pulumi.get(self, "cost")

    @cost.setter
    def cost(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cost", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the hint, used internally to handle the CTFd corresponding object.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def requirements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Other hints required to be consumed before getting this one. Useful for cost-increasing hint strategies with more and more help.
        """
        return pulumi.get(self, "requirements")

    @requirements.setter
    def requirements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "requirements", value)


@pulumi.input_type
class ChallengeRequirementsArgs:
    def __init__(__self__, *,
                 behavior: Optional[pulumi.Input[str]] = None,
                 prerequisites: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] behavior: Behavior if not unlocked, either hidden or anonymized.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prerequisites: List of the challenges ID.
        """
        if behavior is not None:
            pulumi.set(__self__, "behavior", behavior)
        if prerequisites is not None:
            pulumi.set(__self__, "prerequisites", prerequisites)

    @property
    @pulumi.getter
    def behavior(self) -> Optional[pulumi.Input[str]]:
        """
        Behavior if not unlocked, either hidden or anonymized.
        """
        return pulumi.get(self, "behavior")

    @behavior.setter
    def behavior(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "behavior", value)

    @property
    @pulumi.getter
    def prerequisites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of the challenges ID.
        """
        return pulumi.get(self, "prerequisites")

    @prerequisites.setter
    def prerequisites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "prerequisites", value)


