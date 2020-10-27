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
from swagger_client.models.creation_date import CreationDate  # noqa: F401,E501
from swagger_client.models.date_created import DateCreated  # noqa: F401,E501
from swagger_client.models.date_modified import DateModified  # noqa: F401,E501
from swagger_client.models.debit_party_array import DebitPartyArray  # noqa: F401,E501
from swagger_client.models.description_text import DescriptionText  # noqa: F401,E501
from swagger_client.models.fees_array import FeesArray  # noqa: F401,E501
from swagger_client.models.geo_code import GeoCode  # noqa: F401,E501
from swagger_client.models.metadata_array import MetadataArray  # noqa: F401,E501
from swagger_client.models.modification_date import ModificationDate  # noqa: F401,E501
from swagger_client.models.object import Object  # noqa: F401,E501
from swagger_client.models.original_transaction_reference import OriginalTransactionReference  # noqa: F401,E501
from swagger_client.models.receiving_lei import ReceivingLei  # noqa: F401,E501
from swagger_client.models.request_date import RequestDate  # noqa: F401,E501
from swagger_client.models.requesting_lei import RequestingLei  # noqa: F401,E501
from swagger_client.models.requesting_organisation_transaction_reference import RequestingOrganisationTransactionReference  # noqa: F401,E501
from swagger_client.models.servicing_identity import ServicingIdentity  # noqa: F401,E501
from swagger_client.models.sub_type import SubType  # noqa: F401,E501
from swagger_client.models.transaction_receipt import TransactionReceipt  # noqa: F401,E501
from swagger_client.models.transaction_reference import TransactionReference  # noqa: F401,E501
from swagger_client.models.transaction_status import TransactionStatus  # noqa: F401,E501
from swagger_client.models.type_reversal import TypeReversal  # noqa: F401,E501


class ResponseReversal(object):
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
        'amount': 'Object',
        'currency': 'Object',
        'type': 'TypeReversal',
        'sub_type': 'SubType',
        'description_text': 'DescriptionText',
        'request_date': 'RequestDate',
        'geo_code': 'GeoCode',
        'requesting_organisation_transaction_reference': 'RequestingOrganisationTransactionReference',
        'debit_party': 'DebitPartyArray',
        'credit_party': 'DebitPartyArray',
        'requesting_lei': 'RequestingLei',
        'receiving_lei': 'ReceivingLei',
        'servicing_identity': 'ServicingIdentity',
        'fees': 'FeesArray',
        'metadata': 'MetadataArray',
        'transaction_status': 'TransactionStatus',
        'creation_date': 'CreationDate',
        'modification_date': 'ModificationDate',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified',
        'transaction_reference': 'TransactionReference',
        'transaction_receipt': 'TransactionReceipt',
        'original_transaction_reference': 'OriginalTransactionReference'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'type': 'type',
        'sub_type': 'subType',
        'description_text': 'descriptionText',
        'request_date': 'requestDate',
        'geo_code': 'geoCode',
        'requesting_organisation_transaction_reference': 'requestingOrganisationTransactionReference',
        'debit_party': 'debitParty',
        'credit_party': 'creditParty',
        'requesting_lei': 'requestingLei',
        'receiving_lei': 'receivingLei',
        'servicing_identity': 'servicingIdentity',
        'fees': 'fees',
        'metadata': 'metadata',
        'transaction_status': 'transactionStatus',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate',
        'date_created': 'dateCreated',
        'date_modified': 'dateModified',
        'transaction_reference': 'transactionReference',
        'transaction_receipt': 'transactionReceipt',
        'original_transaction_reference': 'originalTransactionReference'
    }

    def __init__(self, amount=None, currency=None, type=None, sub_type=None, description_text=None, request_date=None, geo_code=None, requesting_organisation_transaction_reference=None, debit_party=None, credit_party=None, requesting_lei=None, receiving_lei=None, servicing_identity=None, fees=None, metadata=None, transaction_status=None, creation_date=None, modification_date=None, date_created=None, date_modified=None, transaction_reference=None, transaction_receipt=None, original_transaction_reference=None):  # noqa: E501
        """ResponseReversal - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self._type = None
        self._sub_type = None
        self._description_text = None
        self._request_date = None
        self._geo_code = None
        self._requesting_organisation_transaction_reference = None
        self._debit_party = None
        self._credit_party = None
        self._requesting_lei = None
        self._receiving_lei = None
        self._servicing_identity = None
        self._fees = None
        self._metadata = None
        self._transaction_status = None
        self._creation_date = None
        self._modification_date = None
        self._date_created = None
        self._date_modified = None
        self._transaction_reference = None
        self._transaction_receipt = None
        self._original_transaction_reference = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if description_text is not None:
            self.description_text = description_text
        if request_date is not None:
            self.request_date = request_date
        if geo_code is not None:
            self.geo_code = geo_code
        if requesting_organisation_transaction_reference is not None:
            self.requesting_organisation_transaction_reference = requesting_organisation_transaction_reference
        if debit_party is not None:
            self.debit_party = debit_party
        if credit_party is not None:
            self.credit_party = credit_party
        if requesting_lei is not None:
            self.requesting_lei = requesting_lei
        if receiving_lei is not None:
            self.receiving_lei = receiving_lei
        if servicing_identity is not None:
            self.servicing_identity = servicing_identity
        if fees is not None:
            self.fees = fees
        if metadata is not None:
            self.metadata = metadata
        self.transaction_status = transaction_status
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified
        self.transaction_reference = transaction_reference
        if transaction_receipt is not None:
            self.transaction_receipt = transaction_receipt
        self.original_transaction_reference = original_transaction_reference

    @property
    def amount(self):
        """Gets the amount of this ResponseReversal.  # noqa: E501

        The transaction amount.  # noqa: E501

        :return: The amount of this ResponseReversal.  # noqa: E501
        :rtype: Object
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ResponseReversal.

        The transaction amount.  # noqa: E501

        :param amount: The amount of this ResponseReversal.  # noqa: E501
        :type: Object
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this ResponseReversal.  # noqa: E501

        Currency of the transaction amount.  # noqa: E501

        :return: The currency of this ResponseReversal.  # noqa: E501
        :rtype: Object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ResponseReversal.

        Currency of the transaction amount.  # noqa: E501

        :param currency: The currency of this ResponseReversal.  # noqa: E501
        :type: Object
        """

        self._currency = currency

    @property
    def type(self):
        """Gets the type of this ResponseReversal.  # noqa: E501


        :return: The type of this ResponseReversal.  # noqa: E501
        :rtype: TypeReversal
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseReversal.


        :param type: The type of this ResponseReversal.  # noqa: E501
        :type: TypeReversal
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this ResponseReversal.  # noqa: E501


        :return: The sub_type of this ResponseReversal.  # noqa: E501
        :rtype: SubType
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this ResponseReversal.


        :param sub_type: The sub_type of this ResponseReversal.  # noqa: E501
        :type: SubType
        """

        self._sub_type = sub_type

    @property
    def description_text(self):
        """Gets the description_text of this ResponseReversal.  # noqa: E501


        :return: The description_text of this ResponseReversal.  # noqa: E501
        :rtype: DescriptionText
        """
        return self._description_text

    @description_text.setter
    def description_text(self, description_text):
        """Sets the description_text of this ResponseReversal.


        :param description_text: The description_text of this ResponseReversal.  # noqa: E501
        :type: DescriptionText
        """

        self._description_text = description_text

    @property
    def request_date(self):
        """Gets the request_date of this ResponseReversal.  # noqa: E501


        :return: The request_date of this ResponseReversal.  # noqa: E501
        :rtype: RequestDate
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this ResponseReversal.


        :param request_date: The request_date of this ResponseReversal.  # noqa: E501
        :type: RequestDate
        """

        self._request_date = request_date

    @property
    def geo_code(self):
        """Gets the geo_code of this ResponseReversal.  # noqa: E501


        :return: The geo_code of this ResponseReversal.  # noqa: E501
        :rtype: GeoCode
        """
        return self._geo_code

    @geo_code.setter
    def geo_code(self, geo_code):
        """Sets the geo_code of this ResponseReversal.


        :param geo_code: The geo_code of this ResponseReversal.  # noqa: E501
        :type: GeoCode
        """

        self._geo_code = geo_code

    @property
    def requesting_organisation_transaction_reference(self):
        """Gets the requesting_organisation_transaction_reference of this ResponseReversal.  # noqa: E501


        :return: The requesting_organisation_transaction_reference of this ResponseReversal.  # noqa: E501
        :rtype: RequestingOrganisationTransactionReference
        """
        return self._requesting_organisation_transaction_reference

    @requesting_organisation_transaction_reference.setter
    def requesting_organisation_transaction_reference(self, requesting_organisation_transaction_reference):
        """Sets the requesting_organisation_transaction_reference of this ResponseReversal.


        :param requesting_organisation_transaction_reference: The requesting_organisation_transaction_reference of this ResponseReversal.  # noqa: E501
        :type: RequestingOrganisationTransactionReference
        """

        self._requesting_organisation_transaction_reference = requesting_organisation_transaction_reference

    @property
    def debit_party(self):
        """Gets the debit_party of this ResponseReversal.  # noqa: E501


        :return: The debit_party of this ResponseReversal.  # noqa: E501
        :rtype: DebitPartyArray
        """
        return self._debit_party

    @debit_party.setter
    def debit_party(self, debit_party):
        """Sets the debit_party of this ResponseReversal.


        :param debit_party: The debit_party of this ResponseReversal.  # noqa: E501
        :type: DebitPartyArray
        """

        self._debit_party = debit_party

    @property
    def credit_party(self):
        """Gets the credit_party of this ResponseReversal.  # noqa: E501


        :return: The credit_party of this ResponseReversal.  # noqa: E501
        :rtype: DebitPartyArray
        """
        return self._credit_party

    @credit_party.setter
    def credit_party(self, credit_party):
        """Sets the credit_party of this ResponseReversal.


        :param credit_party: The credit_party of this ResponseReversal.  # noqa: E501
        :type: DebitPartyArray
        """

        self._credit_party = credit_party

    @property
    def requesting_lei(self):
        """Gets the requesting_lei of this ResponseReversal.  # noqa: E501


        :return: The requesting_lei of this ResponseReversal.  # noqa: E501
        :rtype: RequestingLei
        """
        return self._requesting_lei

    @requesting_lei.setter
    def requesting_lei(self, requesting_lei):
        """Sets the requesting_lei of this ResponseReversal.


        :param requesting_lei: The requesting_lei of this ResponseReversal.  # noqa: E501
        :type: RequestingLei
        """

        self._requesting_lei = requesting_lei

    @property
    def receiving_lei(self):
        """Gets the receiving_lei of this ResponseReversal.  # noqa: E501


        :return: The receiving_lei of this ResponseReversal.  # noqa: E501
        :rtype: ReceivingLei
        """
        return self._receiving_lei

    @receiving_lei.setter
    def receiving_lei(self, receiving_lei):
        """Sets the receiving_lei of this ResponseReversal.


        :param receiving_lei: The receiving_lei of this ResponseReversal.  # noqa: E501
        :type: ReceivingLei
        """

        self._receiving_lei = receiving_lei

    @property
    def servicing_identity(self):
        """Gets the servicing_identity of this ResponseReversal.  # noqa: E501


        :return: The servicing_identity of this ResponseReversal.  # noqa: E501
        :rtype: ServicingIdentity
        """
        return self._servicing_identity

    @servicing_identity.setter
    def servicing_identity(self, servicing_identity):
        """Sets the servicing_identity of this ResponseReversal.


        :param servicing_identity: The servicing_identity of this ResponseReversal.  # noqa: E501
        :type: ServicingIdentity
        """

        self._servicing_identity = servicing_identity

    @property
    def fees(self):
        """Gets the fees of this ResponseReversal.  # noqa: E501


        :return: The fees of this ResponseReversal.  # noqa: E501
        :rtype: FeesArray
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this ResponseReversal.


        :param fees: The fees of this ResponseReversal.  # noqa: E501
        :type: FeesArray
        """

        self._fees = fees

    @property
    def metadata(self):
        """Gets the metadata of this ResponseReversal.  # noqa: E501


        :return: The metadata of this ResponseReversal.  # noqa: E501
        :rtype: MetadataArray
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ResponseReversal.


        :param metadata: The metadata of this ResponseReversal.  # noqa: E501
        :type: MetadataArray
        """

        self._metadata = metadata

    @property
    def transaction_status(self):
        """Gets the transaction_status of this ResponseReversal.  # noqa: E501


        :return: The transaction_status of this ResponseReversal.  # noqa: E501
        :rtype: TransactionStatus
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this ResponseReversal.


        :param transaction_status: The transaction_status of this ResponseReversal.  # noqa: E501
        :type: TransactionStatus
        """
        if transaction_status is None:
            raise ValueError("Invalid value for `transaction_status`, must not be `None`")  # noqa: E501

        self._transaction_status = transaction_status

    @property
    def creation_date(self):
        """Gets the creation_date of this ResponseReversal.  # noqa: E501


        :return: The creation_date of this ResponseReversal.  # noqa: E501
        :rtype: CreationDate
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ResponseReversal.


        :param creation_date: The creation_date of this ResponseReversal.  # noqa: E501
        :type: CreationDate
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this ResponseReversal.  # noqa: E501


        :return: The modification_date of this ResponseReversal.  # noqa: E501
        :rtype: ModificationDate
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this ResponseReversal.


        :param modification_date: The modification_date of this ResponseReversal.  # noqa: E501
        :type: ModificationDate
        """

        self._modification_date = modification_date

    @property
    def date_created(self):
        """Gets the date_created of this ResponseReversal.  # noqa: E501


        :return: The date_created of this ResponseReversal.  # noqa: E501
        :rtype: DateCreated
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ResponseReversal.


        :param date_created: The date_created of this ResponseReversal.  # noqa: E501
        :type: DateCreated
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ResponseReversal.  # noqa: E501


        :return: The date_modified of this ResponseReversal.  # noqa: E501
        :rtype: DateModified
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ResponseReversal.


        :param date_modified: The date_modified of this ResponseReversal.  # noqa: E501
        :type: DateModified
        """

        self._date_modified = date_modified

    @property
    def transaction_reference(self):
        """Gets the transaction_reference of this ResponseReversal.  # noqa: E501


        :return: The transaction_reference of this ResponseReversal.  # noqa: E501
        :rtype: TransactionReference
        """
        return self._transaction_reference

    @transaction_reference.setter
    def transaction_reference(self, transaction_reference):
        """Sets the transaction_reference of this ResponseReversal.


        :param transaction_reference: The transaction_reference of this ResponseReversal.  # noqa: E501
        :type: TransactionReference
        """
        if transaction_reference is None:
            raise ValueError("Invalid value for `transaction_reference`, must not be `None`")  # noqa: E501

        self._transaction_reference = transaction_reference

    @property
    def transaction_receipt(self):
        """Gets the transaction_receipt of this ResponseReversal.  # noqa: E501


        :return: The transaction_receipt of this ResponseReversal.  # noqa: E501
        :rtype: TransactionReceipt
        """
        return self._transaction_receipt

    @transaction_receipt.setter
    def transaction_receipt(self, transaction_receipt):
        """Sets the transaction_receipt of this ResponseReversal.


        :param transaction_receipt: The transaction_receipt of this ResponseReversal.  # noqa: E501
        :type: TransactionReceipt
        """

        self._transaction_receipt = transaction_receipt

    @property
    def original_transaction_reference(self):
        """Gets the original_transaction_reference of this ResponseReversal.  # noqa: E501


        :return: The original_transaction_reference of this ResponseReversal.  # noqa: E501
        :rtype: OriginalTransactionReference
        """
        return self._original_transaction_reference

    @original_transaction_reference.setter
    def original_transaction_reference(self, original_transaction_reference):
        """Sets the original_transaction_reference of this ResponseReversal.


        :param original_transaction_reference: The original_transaction_reference of this ResponseReversal.  # noqa: E501
        :type: OriginalTransactionReference
        """
        if original_transaction_reference is None:
            raise ValueError("Invalid value for `original_transaction_reference`, must not be `None`")  # noqa: E501

        self._original_transaction_reference = original_transaction_reference

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
        if issubclass(ResponseReversal, dict):
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
        if not isinstance(other, ResponseReversal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other