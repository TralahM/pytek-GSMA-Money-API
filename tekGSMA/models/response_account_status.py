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
from swagger_client.models.account_status import AccountStatus  # noqa: F401,E501
from swagger_client.models.object import Object  # noqa: F401,E501
from swagger_client.models.sub_status import SubStatus  # noqa: F401,E501


class ResponseAccountStatus(object):
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
        'account_status': 'AccountStatus',
        'sub_status': 'SubStatus',
        'lei': 'Object'
    }

    attribute_map = {
        'account_status': 'accountStatus',
        'sub_status': 'subStatus',
        'lei': 'lei'
    }

    def __init__(self, account_status=None, sub_status=None, lei=None):  # noqa: E501
        """ResponseAccountStatus - a model defined in Swagger"""  # noqa: E501
        self._account_status = None
        self._sub_status = None
        self._lei = None
        self.discriminator = None
        self.account_status = account_status
        if sub_status is not None:
            self.sub_status = sub_status
        if lei is not None:
            self.lei = lei

    @property
    def account_status(self):
        """Gets the account_status of this ResponseAccountStatus.  # noqa: E501


        :return: The account_status of this ResponseAccountStatus.  # noqa: E501
        :rtype: AccountStatus
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this ResponseAccountStatus.


        :param account_status: The account_status of this ResponseAccountStatus.  # noqa: E501
        :type: AccountStatus
        """
        if account_status is None:
            raise ValueError("Invalid value for `account_status`, must not be `None`")  # noqa: E501

        self._account_status = account_status

    @property
    def sub_status(self):
        """Gets the sub_status of this ResponseAccountStatus.  # noqa: E501


        :return: The sub_status of this ResponseAccountStatus.  # noqa: E501
        :rtype: SubStatus
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        """Sets the sub_status of this ResponseAccountStatus.


        :param sub_status: The sub_status of this ResponseAccountStatus.  # noqa: E501
        :type: SubStatus
        """

        self._sub_status = sub_status

    @property
    def lei(self):
        """Gets the lei of this ResponseAccountStatus.  # noqa: E501

        Indicates the Legal Entity Identifier of the organisation holding the account.  # noqa: E501

        :return: The lei of this ResponseAccountStatus.  # noqa: E501
        :rtype: Object
        """
        return self._lei

    @lei.setter
    def lei(self, lei):
        """Sets the lei of this ResponseAccountStatus.

        Indicates the Legal Entity Identifier of the organisation holding the account.  # noqa: E501

        :param lei: The lei of this ResponseAccountStatus.  # noqa: E501
        :type: Object
        """

        self._lei = lei

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
        if issubclass(ResponseAccountStatus, dict):
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
        if not isinstance(other, ResponseAccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
