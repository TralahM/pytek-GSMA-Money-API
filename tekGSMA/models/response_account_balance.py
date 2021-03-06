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


class ResponseAccountBalance(object):
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
        'current_balance': 'Object',
        'available_balance': 'Object',
        'reserved_balance': 'Object',
        'uncleared_balance': 'Object',
        'currency': 'Object',
        'account_status': 'AccountStatus'
    }

    attribute_map = {
        'current_balance': 'currentBalance',
        'available_balance': 'availableBalance',
        'reserved_balance': 'reservedBalance',
        'uncleared_balance': 'unclearedBalance',
        'currency': 'currency',
        'account_status': 'accountStatus'
    }

    def __init__(self, current_balance=None, available_balance=None, reserved_balance=None, uncleared_balance=None, currency=None, account_status=None):  # noqa: E501
        """ResponseAccountBalance - a model defined in Swagger"""  # noqa: E501
        self._current_balance = None
        self._available_balance = None
        self._reserved_balance = None
        self._uncleared_balance = None
        self._currency = None
        self._account_status = None
        self.discriminator = None
        if current_balance is not None:
            self.current_balance = current_balance
        if available_balance is not None:
            self.available_balance = available_balance
        if reserved_balance is not None:
            self.reserved_balance = reserved_balance
        if uncleared_balance is not None:
            self.uncleared_balance = uncleared_balance
        if currency is not None:
            self.currency = currency
        if account_status is not None:
            self.account_status = account_status

    @property
    def current_balance(self):
        """Gets the current_balance of this ResponseAccountBalance.  # noqa: E501

        Current outstanding balance on the account.  # noqa: E501

        :return: The current_balance of this ResponseAccountBalance.  # noqa: E501
        :rtype: Object
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this ResponseAccountBalance.

        Current outstanding balance on the account.  # noqa: E501

        :param current_balance: The current_balance of this ResponseAccountBalance.  # noqa: E501
        :type: Object
        """

        self._current_balance = current_balance

    @property
    def available_balance(self):
        """Gets the available_balance of this ResponseAccountBalance.  # noqa: E501

        Indicates the balance that is able to be debited for an account. This balance is only provided on some API provider systems.  # noqa: E501

        :return: The available_balance of this ResponseAccountBalance.  # noqa: E501
        :rtype: Object
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this ResponseAccountBalance.

        Indicates the balance that is able to be debited for an account. This balance is only provided on some API provider systems.  # noqa: E501

        :param available_balance: The available_balance of this ResponseAccountBalance.  # noqa: E501
        :type: Object
        """

        self._available_balance = available_balance

    @property
    def reserved_balance(self):
        """Gets the reserved_balance of this ResponseAccountBalance.  # noqa: E501

        Indicates the portion of the balance that is reserved, i.e. intended to be debited. This balance is only provided on some API provider systems.\"  # noqa: E501

        :return: The reserved_balance of this ResponseAccountBalance.  # noqa: E501
        :rtype: Object
        """
        return self._reserved_balance

    @reserved_balance.setter
    def reserved_balance(self, reserved_balance):
        """Sets the reserved_balance of this ResponseAccountBalance.

        Indicates the portion of the balance that is reserved, i.e. intended to be debited. This balance is only provided on some API provider systems.\"  # noqa: E501

        :param reserved_balance: The reserved_balance of this ResponseAccountBalance.  # noqa: E501
        :type: Object
        """

        self._reserved_balance = reserved_balance

    @property
    def uncleared_balance(self):
        """Gets the uncleared_balance of this ResponseAccountBalance.  # noqa: E501

        Indicates the sum of uncleared funds in an account, i.e. the funds that are awaiting a credit confirmation.  # noqa: E501

        :return: The uncleared_balance of this ResponseAccountBalance.  # noqa: E501
        :rtype: Object
        """
        return self._uncleared_balance

    @uncleared_balance.setter
    def uncleared_balance(self, uncleared_balance):
        """Sets the uncleared_balance of this ResponseAccountBalance.

        Indicates the sum of uncleared funds in an account, i.e. the funds that are awaiting a credit confirmation.  # noqa: E501

        :param uncleared_balance: The uncleared_balance of this ResponseAccountBalance.  # noqa: E501
        :type: Object
        """

        self._uncleared_balance = uncleared_balance

    @property
    def currency(self):
        """Gets the currency of this ResponseAccountBalance.  # noqa: E501

        Currency for all returned balances.  # noqa: E501

        :return: The currency of this ResponseAccountBalance.  # noqa: E501
        :rtype: Object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ResponseAccountBalance.

        Currency for all returned balances.  # noqa: E501

        :param currency: The currency of this ResponseAccountBalance.  # noqa: E501
        :type: Object
        """

        self._currency = currency

    @property
    def account_status(self):
        """Gets the account_status of this ResponseAccountBalance.  # noqa: E501


        :return: The account_status of this ResponseAccountBalance.  # noqa: E501
        :rtype: AccountStatus
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this ResponseAccountBalance.


        :param account_status: The account_status of this ResponseAccountBalance.  # noqa: E501
        :type: AccountStatus
        """

        self._account_status = account_status

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
        if issubclass(ResponseAccountBalance, dict):
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
        if not isinstance(other, ResponseAccountBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
