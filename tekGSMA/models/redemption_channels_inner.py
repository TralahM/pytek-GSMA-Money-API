# coding: utf-8

"""
    Mobile Money API

    This document defines the RESTful endpoints provided by the GSMA Mobile Money API You can find out more about what the API can do for your business at [https://developer.mobilemoneyapi.io]   # noqa: E501

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RedemptionChannelsInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel_type': 'str'
    }

    attribute_map = {
        'channel_type': 'channelType'
    }

    def __init__(self, channel_type=None):  # noqa: E501
        """RedemptionChannelsInner - a model defined in Swagger"""  # noqa: E501
        self._channel_type = None
        self.discriminator = None
        self.channel_type = channel_type

    @property
    def channel_type(self):
        """Gets the channel_type of this RedemptionChannelsInner.  # noqa: E501

        Identifies the channel type  # noqa: E501

        :return: The channel_type of this RedemptionChannelsInner.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this RedemptionChannelsInner.

        Identifies the channel type  # noqa: E501

        :param channel_type: The channel_type of this RedemptionChannelsInner.  # noqa: E501
        :type: str
        """
        if channel_type is None:
            raise ValueError("Invalid value for `channel_type`, must not be `None`")  # noqa: E501

        self._channel_type = channel_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RedemptionChannelsInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RedemptionChannelsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
