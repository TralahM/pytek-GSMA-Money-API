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
from swagger_client.models.fees_array import FeesArray  # noqa: F401,E501
from swagger_client.models.fx_rate import FxRate  # noqa: F401,E501
from swagger_client.models.object import Object  # noqa: F401,E501
from swagger_client.models.quote_expiry_time import QuoteExpiryTime  # noqa: F401,E501
from swagger_client.models.quote_id import QuoteId  # noqa: F401,E501
from swagger_client.models.receiving_service_provider import ReceivingServiceProvider  # noqa: F401,E501


class Quotes(object):
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
        'quote_id': 'QuoteId',
        'quote_expiry_time': 'QuoteExpiryTime',
        'receiving_service_provider': 'ReceivingServiceProvider',
        'sending_amount': 'Object',
        'sending_currency': 'Object',
        'receiving_amount': 'Object',
        'receiving_currency': 'Object',
        'fx_rate': 'FxRate',
        'delivery_method': 'Object',
        'fees': 'FeesArray'
    }

    attribute_map = {
        'quote_id': 'quoteId',
        'quote_expiry_time': 'quoteExpiryTime',
        'receiving_service_provider': 'receivingServiceProvider',
        'sending_amount': 'sendingAmount',
        'sending_currency': 'sendingCurrency',
        'receiving_amount': 'receivingAmount',
        'receiving_currency': 'receivingCurrency',
        'fx_rate': 'fxRate',
        'delivery_method': 'deliveryMethod',
        'fees': 'fees'
    }

    def __init__(self, quote_id=None, quote_expiry_time=None, receiving_service_provider=None, sending_amount=None, sending_currency=None, receiving_amount=None, receiving_currency=None, fx_rate=None, delivery_method=None, fees=None):  # noqa: E501
        """Quotes - a model defined in Swagger"""  # noqa: E501
        self._quote_id = None
        self._quote_expiry_time = None
        self._receiving_service_provider = None
        self._sending_amount = None
        self._sending_currency = None
        self._receiving_amount = None
        self._receiving_currency = None
        self._fx_rate = None
        self._delivery_method = None
        self._fees = None
        self.discriminator = None
        self.quote_id = quote_id
        if quote_expiry_time is not None:
            self.quote_expiry_time = quote_expiry_time
        if receiving_service_provider is not None:
            self.receiving_service_provider = receiving_service_provider
        self.sending_amount = sending_amount
        self.sending_currency = sending_currency
        self.receiving_amount = receiving_amount
        self.receiving_currency = receiving_currency
        if fx_rate is not None:
            self.fx_rate = fx_rate
        if delivery_method is not None:
            self.delivery_method = delivery_method
        if fees is not None:
            self.fees = fees

    @property
    def quote_id(self):
        """Gets the quote_id of this Quotes.  # noqa: E501


        :return: The quote_id of this Quotes.  # noqa: E501
        :rtype: QuoteId
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this Quotes.


        :param quote_id: The quote_id of this Quotes.  # noqa: E501
        :type: QuoteId
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def quote_expiry_time(self):
        """Gets the quote_expiry_time of this Quotes.  # noqa: E501


        :return: The quote_expiry_time of this Quotes.  # noqa: E501
        :rtype: QuoteExpiryTime
        """
        return self._quote_expiry_time

    @quote_expiry_time.setter
    def quote_expiry_time(self, quote_expiry_time):
        """Sets the quote_expiry_time of this Quotes.


        :param quote_expiry_time: The quote_expiry_time of this Quotes.  # noqa: E501
        :type: QuoteExpiryTime
        """

        self._quote_expiry_time = quote_expiry_time

    @property
    def receiving_service_provider(self):
        """Gets the receiving_service_provider of this Quotes.  # noqa: E501


        :return: The receiving_service_provider of this Quotes.  # noqa: E501
        :rtype: ReceivingServiceProvider
        """
        return self._receiving_service_provider

    @receiving_service_provider.setter
    def receiving_service_provider(self, receiving_service_provider):
        """Sets the receiving_service_provider of this Quotes.


        :param receiving_service_provider: The receiving_service_provider of this Quotes.  # noqa: E501
        :type: ReceivingServiceProvider
        """

        self._receiving_service_provider = receiving_service_provider

    @property
    def sending_amount(self):
        """Gets the sending_amount of this Quotes.  # noqa: E501

        The requested quotation amount as supplied by the sender.  # noqa: E501

        :return: The sending_amount of this Quotes.  # noqa: E501
        :rtype: Object
        """
        return self._sending_amount

    @sending_amount.setter
    def sending_amount(self, sending_amount):
        """Sets the sending_amount of this Quotes.

        The requested quotation amount as supplied by the sender.  # noqa: E501

        :param sending_amount: The sending_amount of this Quotes.  # noqa: E501
        :type: Object
        """
        if sending_amount is None:
            raise ValueError("Invalid value for `sending_amount`, must not be `None`")  # noqa: E501

        self._sending_amount = sending_amount

    @property
    def sending_currency(self):
        """Gets the sending_currency of this Quotes.  # noqa: E501

        Currency of the requested quotation amount.  # noqa: E501

        :return: The sending_currency of this Quotes.  # noqa: E501
        :rtype: Object
        """
        return self._sending_currency

    @sending_currency.setter
    def sending_currency(self, sending_currency):
        """Sets the sending_currency of this Quotes.

        Currency of the requested quotation amount.  # noqa: E501

        :param sending_currency: The sending_currency of this Quotes.  # noqa: E501
        :type: Object
        """
        if sending_currency is None:
            raise ValueError("Invalid value for `sending_currency`, must not be `None`")  # noqa: E501

        self._sending_currency = sending_currency

    @property
    def receiving_amount(self):
        """Gets the receiving_amount of this Quotes.  # noqa: E501

        The total amount as it will be received by the receiving end-user.  # noqa: E501

        :return: The receiving_amount of this Quotes.  # noqa: E501
        :rtype: Object
        """
        return self._receiving_amount

    @receiving_amount.setter
    def receiving_amount(self, receiving_amount):
        """Sets the receiving_amount of this Quotes.

        The total amount as it will be received by the receiving end-user.  # noqa: E501

        :param receiving_amount: The receiving_amount of this Quotes.  # noqa: E501
        :type: Object
        """
        if receiving_amount is None:
            raise ValueError("Invalid value for `receiving_amount`, must not be `None`")  # noqa: E501

        self._receiving_amount = receiving_amount

    @property
    def receiving_currency(self):
        """Gets the receiving_currency of this Quotes.  # noqa: E501

        The currency of the quote.  # noqa: E501

        :return: The receiving_currency of this Quotes.  # noqa: E501
        :rtype: Object
        """
        return self._receiving_currency

    @receiving_currency.setter
    def receiving_currency(self, receiving_currency):
        """Sets the receiving_currency of this Quotes.

        The currency of the quote.  # noqa: E501

        :param receiving_currency: The receiving_currency of this Quotes.  # noqa: E501
        :type: Object
        """
        if receiving_currency is None:
            raise ValueError("Invalid value for `receiving_currency`, must not be `None`")  # noqa: E501

        self._receiving_currency = receiving_currency

    @property
    def fx_rate(self):
        """Gets the fx_rate of this Quotes.  # noqa: E501


        :return: The fx_rate of this Quotes.  # noqa: E501
        :rtype: FxRate
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """Sets the fx_rate of this Quotes.


        :param fx_rate: The fx_rate of this Quotes.  # noqa: E501
        :type: FxRate
        """

        self._fx_rate = fx_rate

    @property
    def delivery_method(self):
        """Gets the delivery_method of this Quotes.  # noqa: E501

        The delivery method that is applicable to the quotation.  # noqa: E501

        :return: The delivery_method of this Quotes.  # noqa: E501
        :rtype: Object
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this Quotes.

        The delivery method that is applicable to the quotation.  # noqa: E501

        :param delivery_method: The delivery_method of this Quotes.  # noqa: E501
        :type: Object
        """

        self._delivery_method = delivery_method

    @property
    def fees(self):
        """Gets the fees of this Quotes.  # noqa: E501


        :return: The fees of this Quotes.  # noqa: E501
        :rtype: FeesArray
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this Quotes.


        :param fees: The fees of this Quotes.  # noqa: E501
        :type: FeesArray
        """

        self._fees = fees

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
        if issubclass(Quotes, dict):
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
        if not isinstance(other, Quotes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
