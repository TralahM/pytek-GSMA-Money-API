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
from swagger_client.models.approval_date import ApprovalDate  # noqa: F401,E501
from swagger_client.models.batch_description import BatchDescription  # noqa: F401,E501
from swagger_client.models.batch_id import BatchId  # noqa: F401,E501
from swagger_client.models.batch_status import BatchStatus  # noqa: F401,E501
from swagger_client.models.batch_title import BatchTitle  # noqa: F401,E501
from swagger_client.models.completed_count import CompletedCount  # noqa: F401,E501
from swagger_client.models.completed_date import CompletedDate  # noqa: F401,E501
from swagger_client.models.completion_date import CompletionDate  # noqa: F401,E501
from swagger_client.models.creation_date import CreationDate  # noqa: F401,E501
from swagger_client.models.parsing_success_count import ParsingSuccessCount  # noqa: F401,E501
from swagger_client.models.processing_flag import ProcessingFlag  # noqa: F401,E501
from swagger_client.models.rejection_count import RejectionCount  # noqa: F401,E501
from swagger_client.models.scheduled_start_date import ScheduledStartDate  # noqa: F401,E501


class ResponseBatchTransaction(object):
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
        'batch_title': 'BatchTitle',
        'batchdescription': 'BatchDescription',
        'processing_flag': 'ProcessingFlag',
        'scheduled_start_date': 'ScheduledStartDate',
        'batch_status': 'BatchStatus',
        'batch_id': 'BatchId',
        'creation_date': 'CreationDate',
        'approval_date': 'ApprovalDate',
        'completion_date': 'CompletionDate',
        'completed_date': 'CompletedDate',
        'rejection_count': 'RejectionCount',
        'parsing_success_count': 'ParsingSuccessCount',
        'completed_count': 'CompletedCount'
    }

    attribute_map = {
        'batch_title': 'batchTitle',
        'batchdescription': 'batchdescription',
        'processing_flag': 'processingFlag',
        'scheduled_start_date': 'scheduledStartDate',
        'batch_status': 'batchStatus',
        'batch_id': 'batchId',
        'creation_date': 'creationDate',
        'approval_date': 'approvalDate',
        'completion_date': 'completionDate',
        'completed_date': 'completedDate',
        'rejection_count': 'rejectionCount',
        'parsing_success_count': 'parsingSuccessCount',
        'completed_count': 'completedCount'
    }

    def __init__(self, batch_title=None, batchdescription=None, processing_flag=None, scheduled_start_date=None, batch_status=None, batch_id=None, creation_date=None, approval_date=None, completion_date=None, completed_date=None, rejection_count=None, parsing_success_count=None, completed_count=None):  # noqa: E501
        """ResponseBatchTransaction - a model defined in Swagger"""  # noqa: E501
        self._batch_title = None
        self._batchdescription = None
        self._processing_flag = None
        self._scheduled_start_date = None
        self._batch_status = None
        self._batch_id = None
        self._creation_date = None
        self._approval_date = None
        self._completion_date = None
        self._completed_date = None
        self._rejection_count = None
        self._parsing_success_count = None
        self._completed_count = None
        self.discriminator = None
        if batch_title is not None:
            self.batch_title = batch_title
        if batchdescription is not None:
            self.batchdescription = batchdescription
        if processing_flag is not None:
            self.processing_flag = processing_flag
        if scheduled_start_date is not None:
            self.scheduled_start_date = scheduled_start_date
        self.batch_status = batch_status
        self.batch_id = batch_id
        self.creation_date = creation_date
        self.approval_date = approval_date
        self.completion_date = completion_date
        if completed_date is not None:
            self.completed_date = completed_date
        if rejection_count is not None:
            self.rejection_count = rejection_count
        if parsing_success_count is not None:
            self.parsing_success_count = parsing_success_count
        if completed_count is not None:
            self.completed_count = completed_count

    @property
    def batch_title(self):
        """Gets the batch_title of this ResponseBatchTransaction.  # noqa: E501


        :return: The batch_title of this ResponseBatchTransaction.  # noqa: E501
        :rtype: BatchTitle
        """
        return self._batch_title

    @batch_title.setter
    def batch_title(self, batch_title):
        """Sets the batch_title of this ResponseBatchTransaction.


        :param batch_title: The batch_title of this ResponseBatchTransaction.  # noqa: E501
        :type: BatchTitle
        """

        self._batch_title = batch_title

    @property
    def batchdescription(self):
        """Gets the batchdescription of this ResponseBatchTransaction.  # noqa: E501


        :return: The batchdescription of this ResponseBatchTransaction.  # noqa: E501
        :rtype: BatchDescription
        """
        return self._batchdescription

    @batchdescription.setter
    def batchdescription(self, batchdescription):
        """Sets the batchdescription of this ResponseBatchTransaction.


        :param batchdescription: The batchdescription of this ResponseBatchTransaction.  # noqa: E501
        :type: BatchDescription
        """

        self._batchdescription = batchdescription

    @property
    def processing_flag(self):
        """Gets the processing_flag of this ResponseBatchTransaction.  # noqa: E501


        :return: The processing_flag of this ResponseBatchTransaction.  # noqa: E501
        :rtype: ProcessingFlag
        """
        return self._processing_flag

    @processing_flag.setter
    def processing_flag(self, processing_flag):
        """Sets the processing_flag of this ResponseBatchTransaction.


        :param processing_flag: The processing_flag of this ResponseBatchTransaction.  # noqa: E501
        :type: ProcessingFlag
        """

        self._processing_flag = processing_flag

    @property
    def scheduled_start_date(self):
        """Gets the scheduled_start_date of this ResponseBatchTransaction.  # noqa: E501


        :return: The scheduled_start_date of this ResponseBatchTransaction.  # noqa: E501
        :rtype: ScheduledStartDate
        """
        return self._scheduled_start_date

    @scheduled_start_date.setter
    def scheduled_start_date(self, scheduled_start_date):
        """Sets the scheduled_start_date of this ResponseBatchTransaction.


        :param scheduled_start_date: The scheduled_start_date of this ResponseBatchTransaction.  # noqa: E501
        :type: ScheduledStartDate
        """

        self._scheduled_start_date = scheduled_start_date

    @property
    def batch_status(self):
        """Gets the batch_status of this ResponseBatchTransaction.  # noqa: E501


        :return: The batch_status of this ResponseBatchTransaction.  # noqa: E501
        :rtype: BatchStatus
        """
        return self._batch_status

    @batch_status.setter
    def batch_status(self, batch_status):
        """Sets the batch_status of this ResponseBatchTransaction.


        :param batch_status: The batch_status of this ResponseBatchTransaction.  # noqa: E501
        :type: BatchStatus
        """
        if batch_status is None:
            raise ValueError("Invalid value for `batch_status`, must not be `None`")  # noqa: E501

        self._batch_status = batch_status

    @property
    def batch_id(self):
        """Gets the batch_id of this ResponseBatchTransaction.  # noqa: E501


        :return: The batch_id of this ResponseBatchTransaction.  # noqa: E501
        :rtype: BatchId
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this ResponseBatchTransaction.


        :param batch_id: The batch_id of this ResponseBatchTransaction.  # noqa: E501
        :type: BatchId
        """
        if batch_id is None:
            raise ValueError("Invalid value for `batch_id`, must not be `None`")  # noqa: E501

        self._batch_id = batch_id

    @property
    def creation_date(self):
        """Gets the creation_date of this ResponseBatchTransaction.  # noqa: E501


        :return: The creation_date of this ResponseBatchTransaction.  # noqa: E501
        :rtype: CreationDate
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ResponseBatchTransaction.


        :param creation_date: The creation_date of this ResponseBatchTransaction.  # noqa: E501
        :type: CreationDate
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def approval_date(self):
        """Gets the approval_date of this ResponseBatchTransaction.  # noqa: E501


        :return: The approval_date of this ResponseBatchTransaction.  # noqa: E501
        :rtype: ApprovalDate
        """
        return self._approval_date

    @approval_date.setter
    def approval_date(self, approval_date):
        """Sets the approval_date of this ResponseBatchTransaction.


        :param approval_date: The approval_date of this ResponseBatchTransaction.  # noqa: E501
        :type: ApprovalDate
        """
        if approval_date is None:
            raise ValueError("Invalid value for `approval_date`, must not be `None`")  # noqa: E501

        self._approval_date = approval_date

    @property
    def completion_date(self):
        """Gets the completion_date of this ResponseBatchTransaction.  # noqa: E501


        :return: The completion_date of this ResponseBatchTransaction.  # noqa: E501
        :rtype: CompletionDate
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this ResponseBatchTransaction.


        :param completion_date: The completion_date of this ResponseBatchTransaction.  # noqa: E501
        :type: CompletionDate
        """
        if completion_date is None:
            raise ValueError("Invalid value for `completion_date`, must not be `None`")  # noqa: E501

        self._completion_date = completion_date

    @property
    def completed_date(self):
        """Gets the completed_date of this ResponseBatchTransaction.  # noqa: E501


        :return: The completed_date of this ResponseBatchTransaction.  # noqa: E501
        :rtype: CompletedDate
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this ResponseBatchTransaction.


        :param completed_date: The completed_date of this ResponseBatchTransaction.  # noqa: E501
        :type: CompletedDate
        """

        self._completed_date = completed_date

    @property
    def rejection_count(self):
        """Gets the rejection_count of this ResponseBatchTransaction.  # noqa: E501


        :return: The rejection_count of this ResponseBatchTransaction.  # noqa: E501
        :rtype: RejectionCount
        """
        return self._rejection_count

    @rejection_count.setter
    def rejection_count(self, rejection_count):
        """Sets the rejection_count of this ResponseBatchTransaction.


        :param rejection_count: The rejection_count of this ResponseBatchTransaction.  # noqa: E501
        :type: RejectionCount
        """

        self._rejection_count = rejection_count

    @property
    def parsing_success_count(self):
        """Gets the parsing_success_count of this ResponseBatchTransaction.  # noqa: E501


        :return: The parsing_success_count of this ResponseBatchTransaction.  # noqa: E501
        :rtype: ParsingSuccessCount
        """
        return self._parsing_success_count

    @parsing_success_count.setter
    def parsing_success_count(self, parsing_success_count):
        """Sets the parsing_success_count of this ResponseBatchTransaction.


        :param parsing_success_count: The parsing_success_count of this ResponseBatchTransaction.  # noqa: E501
        :type: ParsingSuccessCount
        """

        self._parsing_success_count = parsing_success_count

    @property
    def completed_count(self):
        """Gets the completed_count of this ResponseBatchTransaction.  # noqa: E501


        :return: The completed_count of this ResponseBatchTransaction.  # noqa: E501
        :rtype: CompletedCount
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """Sets the completed_count of this ResponseBatchTransaction.


        :param completed_count: The completed_count of this ResponseBatchTransaction.  # noqa: E501
        :type: CompletedCount
        """

        self._completed_count = completed_count

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
        if issubclass(ResponseBatchTransaction, dict):
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
        if not isinstance(other, ResponseBatchTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
