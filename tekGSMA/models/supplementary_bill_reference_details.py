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


class SupplementaryBillReferenceDetails(object):
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
        'payment_reference_type': 'str',
        'payment_reference_value': 'str'
    }

    attribute_map = {
        'payment_reference_type': 'paymentReferenceType',
        'payment_reference_value': 'paymentReferenceValue'
    }

    def __init__(self, payment_reference_type=None, payment_reference_value=None):  # noqa: E501
        """SupplementaryBillReferenceDetails - a model defined in Swagger"""  # noqa: E501
        self._payment_reference_type = None
        self._payment_reference_value = None
        self.discriminator = None
        self.payment_reference_type = payment_reference_type
        self.payment_reference_value = payment_reference_value

    @property
    def payment_reference_type(self):
        """Gets the payment_reference_type of this SupplementaryBillReferenceDetails.  # noqa: E501

        Identifies the type of the additional payment reference.  # noqa: E501

        :return: The payment_reference_type of this SupplementaryBillReferenceDetails.  # noqa: E501
        :rtype: str
        """
        return self._payment_reference_type

    @payment_reference_type.setter
    def payment_reference_type(self, payment_reference_type):
        """Sets the payment_reference_type of this SupplementaryBillReferenceDetails.

        Identifies the type of the additional payment reference.  # noqa: E501

        :param payment_reference_type: The payment_reference_type of this SupplementaryBillReferenceDetails.  # noqa: E501
        :type: str
        """
        if payment_reference_type is None:
            raise ValueError("Invalid value for `payment_reference_type`, must not be `None`")  # noqa: E501

        self._payment_reference_type = payment_reference_type

    @property
    def payment_reference_value(self):
        """Gets the payment_reference_value of this SupplementaryBillReferenceDetails.  # noqa: E501

        Identifies the value of the additional payment reference.  # noqa: E501

        :return: The payment_reference_value of this SupplementaryBillReferenceDetails.  # noqa: E501
        :rtype: str
        """
        return self._payment_reference_value

    @payment_reference_value.setter
    def payment_reference_value(self, payment_reference_value):
        """Sets the payment_reference_value of this SupplementaryBillReferenceDetails.

        Identifies the value of the additional payment reference.  # noqa: E501

        :param payment_reference_value: The payment_reference_value of this SupplementaryBillReferenceDetails.  # noqa: E501
        :type: str
        """
        if payment_reference_value is None:
            raise ValueError("Invalid value for `payment_reference_value`, must not be `None`")  # noqa: E501

        self._payment_reference_value = payment_reference_value

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
        if issubclass(SupplementaryBillReferenceDetails, dict):
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
        if not isinstance(other, SupplementaryBillReferenceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
