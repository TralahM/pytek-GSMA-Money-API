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
from swagger_client.models.credit_party_array import CreditPartyArray  # noqa: F401,E501
from swagger_client.models.date_rejected import DateRejected  # noqa: F401,E501
from swagger_client.models.debit_party_array import DebitPartyArray  # noqa: F401,E501
from swagger_client.models.rejection_date import RejectionDate  # noqa: F401,E501
from swagger_client.models.rejection_reason import RejectionReason  # noqa: F401,E501
from swagger_client.models.requesting_organisation_transaction_reference import RequestingOrganisationTransactionReference  # noqa: F401,E501
from swagger_client.models.transaction_reference import TransactionReference  # noqa: F401,E501


class ResponseBatchTransactionRejection(object):
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
        'transaction_reference': 'TransactionReference',
        'rejection_date': 'RejectionDate',
        'date_rejected': 'DateRejected',
        'debit_party': 'DebitPartyArray',
        'credit_party': 'CreditPartyArray',
        'rejection_reason': 'RejectionReason',
        'requesting_organisation_transaction_reference': 'RequestingOrganisationTransactionReference'
    }

    attribute_map = {
        'transaction_reference': 'transactionReference',
        'rejection_date': 'rejectionDate',
        'date_rejected': 'dateRejected',
        'debit_party': 'debitParty',
        'credit_party': 'creditParty',
        'rejection_reason': 'rejectionReason',
        'requesting_organisation_transaction_reference': 'requestingOrganisationTransactionReference'
    }

    def __init__(self, transaction_reference=None, rejection_date=None, date_rejected=None, debit_party=None, credit_party=None, rejection_reason=None, requesting_organisation_transaction_reference=None):  # noqa: E501
        """ResponseBatchTransactionRejection - a model defined in Swagger"""  # noqa: E501
        self._transaction_reference = None
        self._rejection_date = None
        self._date_rejected = None
        self._debit_party = None
        self._credit_party = None
        self._rejection_reason = None
        self._requesting_organisation_transaction_reference = None
        self.discriminator = None
        if transaction_reference is not None:
            self.transaction_reference = transaction_reference
        self.rejection_date = rejection_date
        if date_rejected is not None:
            self.date_rejected = date_rejected
        self.debit_party = debit_party
        self.credit_party = credit_party
        self.rejection_reason = rejection_reason
        if requesting_organisation_transaction_reference is not None:
            self.requesting_organisation_transaction_reference = requesting_organisation_transaction_reference

    @property
    def transaction_reference(self):
        """Gets the transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: TransactionReference
        """
        return self._transaction_reference

    @transaction_reference.setter
    def transaction_reference(self, transaction_reference):
        """Sets the transaction_reference of this ResponseBatchTransactionRejection.


        :param transaction_reference: The transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: TransactionReference
        """

        self._transaction_reference = transaction_reference

    @property
    def rejection_date(self):
        """Gets the rejection_date of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The rejection_date of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: RejectionDate
        """
        return self._rejection_date

    @rejection_date.setter
    def rejection_date(self, rejection_date):
        """Sets the rejection_date of this ResponseBatchTransactionRejection.


        :param rejection_date: The rejection_date of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: RejectionDate
        """
        if rejection_date is None:
            raise ValueError("Invalid value for `rejection_date`, must not be `None`")  # noqa: E501

        self._rejection_date = rejection_date

    @property
    def date_rejected(self):
        """Gets the date_rejected of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The date_rejected of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: DateRejected
        """
        return self._date_rejected

    @date_rejected.setter
    def date_rejected(self, date_rejected):
        """Sets the date_rejected of this ResponseBatchTransactionRejection.


        :param date_rejected: The date_rejected of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: DateRejected
        """

        self._date_rejected = date_rejected

    @property
    def debit_party(self):
        """Gets the debit_party of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The debit_party of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: DebitPartyArray
        """
        return self._debit_party

    @debit_party.setter
    def debit_party(self, debit_party):
        """Sets the debit_party of this ResponseBatchTransactionRejection.


        :param debit_party: The debit_party of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: DebitPartyArray
        """
        if debit_party is None:
            raise ValueError("Invalid value for `debit_party`, must not be `None`")  # noqa: E501

        self._debit_party = debit_party

    @property
    def credit_party(self):
        """Gets the credit_party of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The credit_party of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: CreditPartyArray
        """
        return self._credit_party

    @credit_party.setter
    def credit_party(self, credit_party):
        """Sets the credit_party of this ResponseBatchTransactionRejection.


        :param credit_party: The credit_party of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: CreditPartyArray
        """
        if credit_party is None:
            raise ValueError("Invalid value for `credit_party`, must not be `None`")  # noqa: E501

        self._credit_party = credit_party

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The rejection_reason of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: RejectionReason
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this ResponseBatchTransactionRejection.


        :param rejection_reason: The rejection_reason of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: RejectionReason
        """
        if rejection_reason is None:
            raise ValueError("Invalid value for `rejection_reason`, must not be `None`")  # noqa: E501

        self._rejection_reason = rejection_reason

    @property
    def requesting_organisation_transaction_reference(self):
        """Gets the requesting_organisation_transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501


        :return: The requesting_organisation_transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501
        :rtype: RequestingOrganisationTransactionReference
        """
        return self._requesting_organisation_transaction_reference

    @requesting_organisation_transaction_reference.setter
    def requesting_organisation_transaction_reference(self, requesting_organisation_transaction_reference):
        """Sets the requesting_organisation_transaction_reference of this ResponseBatchTransactionRejection.


        :param requesting_organisation_transaction_reference: The requesting_organisation_transaction_reference of this ResponseBatchTransactionRejection.  # noqa: E501
        :type: RequestingOrganisationTransactionReference
        """

        self._requesting_organisation_transaction_reference = requesting_organisation_transaction_reference

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
        if issubclass(ResponseBatchTransactionRejection, dict):
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
        if not isinstance(other, ResponseBatchTransactionRejection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
