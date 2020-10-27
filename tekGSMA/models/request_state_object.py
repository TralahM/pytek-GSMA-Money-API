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
from swagger_client.models.big_decimal import BigDecimal  # noqa: F401,E501
from swagger_client.models.object import Object  # noqa: F401,E501


class RequestStateObject(object):
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
        'server_correlation_id': 'str',
        'status': 'str',
        'pending_reason': 'str',
        'notification_method': 'str',
        'object_reference': 'str',
        'expiry_time': 'datetime',
        'poll_limit': 'BigDecimal',
        'error': 'Object'
    }

    attribute_map = {
        'server_correlation_id': 'serverCorrelationId',
        'status': 'status',
        'pending_reason': 'pendingReason',
        'notification_method': 'notificationMethod',
        'object_reference': 'objectReference',
        'expiry_time': 'expiryTime',
        'poll_limit': 'pollLimit',
        'error': 'error'
    }

    def __init__(self, server_correlation_id=None, status=None, pending_reason=None, notification_method=None, object_reference=None, expiry_time=None, poll_limit=None, error=None):  # noqa: E501
        """RequestStateObject - a model defined in Swagger"""  # noqa: E501
        self._server_correlation_id = None
        self._status = None
        self._pending_reason = None
        self._notification_method = None
        self._object_reference = None
        self._expiry_time = None
        self._poll_limit = None
        self._error = None
        self.discriminator = None
        self.server_correlation_id = server_correlation_id
        self.status = status
        if pending_reason is not None:
            self.pending_reason = pending_reason
        self.notification_method = notification_method
        if object_reference is not None:
            self.object_reference = object_reference
        if expiry_time is not None:
            self.expiry_time = expiry_time
        if poll_limit is not None:
            self.poll_limit = poll_limit
        if error is not None:
            self.error = error

    @property
    def server_correlation_id(self):
        """Gets the server_correlation_id of this RequestStateObject.  # noqa: E501

        A unique identifier issued by the provider to enable the client to identify the RequestState resource on subsequent polling requests. Must be supplied as a UUID.  # noqa: E501

        :return: The server_correlation_id of this RequestStateObject.  # noqa: E501
        :rtype: str
        """
        return self._server_correlation_id

    @server_correlation_id.setter
    def server_correlation_id(self, server_correlation_id):
        """Sets the server_correlation_id of this RequestStateObject.

        A unique identifier issued by the provider to enable the client to identify the RequestState resource on subsequent polling requests. Must be supplied as a UUID.  # noqa: E501

        :param server_correlation_id: The server_correlation_id of this RequestStateObject.  # noqa: E501
        :type: str
        """
        if server_correlation_id is None:
            raise ValueError("Invalid value for `server_correlation_id`, must not be `None`")  # noqa: E501

        self._server_correlation_id = server_correlation_id

    @property
    def status(self):
        """Gets the status of this RequestStateObject.  # noqa: E501

        Indicates the status of the request.  # noqa: E501

        :return: The status of this RequestStateObject.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestStateObject.

        Indicates the status of the request.  # noqa: E501

        :param status: The status of this RequestStateObject.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["pending", "completed", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def pending_reason(self):
        """Gets the pending_reason of this RequestStateObject.  # noqa: E501

        A textual description that can be provided to describe the reason for a pending status.  # noqa: E501

        :return: The pending_reason of this RequestStateObject.  # noqa: E501
        :rtype: str
        """
        return self._pending_reason

    @pending_reason.setter
    def pending_reason(self, pending_reason):
        """Sets the pending_reason of this RequestStateObject.

        A textual description that can be provided to describe the reason for a pending status.  # noqa: E501

        :param pending_reason: The pending_reason of this RequestStateObject.  # noqa: E501
        :type: str
        """

        self._pending_reason = pending_reason

    @property
    def notification_method(self):
        """Gets the notification_method of this RequestStateObject.  # noqa: E501

        Indicates whether a callback will be issued or whether the client will need to poll.  # noqa: E501

        :return: The notification_method of this RequestStateObject.  # noqa: E501
        :rtype: str
        """
        return self._notification_method

    @notification_method.setter
    def notification_method(self, notification_method):
        """Sets the notification_method of this RequestStateObject.

        Indicates whether a callback will be issued or whether the client will need to poll.  # noqa: E501

        :param notification_method: The notification_method of this RequestStateObject.  # noqa: E501
        :type: str
        """
        if notification_method is None:
            raise ValueError("Invalid value for `notification_method`, must not be `None`")  # noqa: E501
        allowed_values = ["callback", "polling"]  # noqa: E501
        if notification_method not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_method` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_method, allowed_values)
            )

        self._notification_method = notification_method

    @property
    def object_reference(self):
        """Gets the object_reference of this RequestStateObject.  # noqa: E501

        Provides a reference to the subject resource, e.g. transaction reference.  # noqa: E501

        :return: The object_reference of this RequestStateObject.  # noqa: E501
        :rtype: str
        """
        return self._object_reference

    @object_reference.setter
    def object_reference(self, object_reference):
        """Sets the object_reference of this RequestStateObject.

        Provides a reference to the subject resource, e.g. transaction reference.  # noqa: E501

        :param object_reference: The object_reference of this RequestStateObject.  # noqa: E501
        :type: str
        """

        self._object_reference = object_reference

    @property
    def expiry_time(self):
        """Gets the expiry_time of this RequestStateObject.  # noqa: E501

        Indicate the time by which the provider will fail the request if completion criteria have not been met. For an example, a debit party failing to authorise within the allowed period.  # noqa: E501

        :return: The expiry_time of this RequestStateObject.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this RequestStateObject.

        Indicate the time by which the provider will fail the request if completion criteria have not been met. For an example, a debit party failing to authorise within the allowed period.  # noqa: E501

        :param expiry_time: The expiry_time of this RequestStateObject.  # noqa: E501
        :type: datetime
        """

        self._expiry_time = expiry_time

    @property
    def poll_limit(self):
        """Gets the poll_limit of this RequestStateObject.  # noqa: E501

        Indicates the number of poll attempts for the given requeststate resource that will be allowed by the provider.  # noqa: E501

        :return: The poll_limit of this RequestStateObject.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._poll_limit

    @poll_limit.setter
    def poll_limit(self, poll_limit):
        """Sets the poll_limit of this RequestStateObject.

        Indicates the number of poll attempts for the given requeststate resource that will be allowed by the provider.  # noqa: E501

        :param poll_limit: The poll_limit of this RequestStateObject.  # noqa: E501
        :type: BigDecimal
        """

        self._poll_limit = poll_limit

    @property
    def error(self):
        """Gets the error of this RequestStateObject.  # noqa: E501

        If the asynchronous processing failed, details of the error will be returned here.  # noqa: E501

        :return: The error of this RequestStateObject.  # noqa: E501
        :rtype: Object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RequestStateObject.

        If the asynchronous processing failed, details of the error will be returned here.  # noqa: E501

        :param error: The error of this RequestStateObject.  # noqa: E501
        :type: Object
        """

        self._error = error

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
        if issubclass(RequestStateObject, dict):
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
        if not isinstance(other, RequestStateObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other