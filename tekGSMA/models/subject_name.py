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


class SubjectName(object):
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
        'title': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'full_name': 'str',
        'native_name': 'str'
    }

    attribute_map = {
        'title': 'title',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'full_name': 'fullName',
        'native_name': 'nativeName'
    }

    def __init__(self, title=None, first_name=None, middle_name=None, last_name=None, full_name=None, native_name=None):  # noqa: E501
        """SubjectName - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._full_name = None
        self._native_name = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if full_name is not None:
            self.full_name = full_name
        if native_name is not None:
            self.native_name = native_name

    @property
    def title(self):
        """Gets the title of this SubjectName.  # noqa: E501

        The given title of the KYC subject, e.g. Mr, Mrs, Dr.  # noqa: E501

        :return: The title of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SubjectName.

        The given title of the KYC subject, e.g. Mr, Mrs, Dr.  # noqa: E501

        :param title: The title of this SubjectName.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """Gets the first_name of this SubjectName.  # noqa: E501

        First name (also referred to as given name) of the KYC subject.  # noqa: E501

        :return: The first_name of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SubjectName.

        First name (also referred to as given name) of the KYC subject.  # noqa: E501

        :param first_name: The first_name of this SubjectName.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this SubjectName.  # noqa: E501

        Middle Name of the KYC subject.  # noqa: E501

        :return: The middle_name of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this SubjectName.

        Middle Name of the KYC subject.  # noqa: E501

        :param middle_name: The middle_name of this SubjectName.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this SubjectName.  # noqa: E501

        Surname (also referred to as last or family name) of the KYC subject.\"  # noqa: E501

        :return: The last_name of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SubjectName.

        Surname (also referred to as last or family name) of the KYC subject.\"  # noqa: E501

        :param last_name: The last_name of this SubjectName.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def full_name(self):
        """Gets the full_name of this SubjectName.  # noqa: E501

        The full name of the KYC subject.  # noqa: E501

        :return: The full_name of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SubjectName.

        The full name of the KYC subject.  # noqa: E501

        :param full_name: The full_name of this SubjectName.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def native_name(self):
        """Gets the native_name of this SubjectName.  # noqa: E501

        The full name expressed as in the native language.  # noqa: E501

        :return: The native_name of this SubjectName.  # noqa: E501
        :rtype: str
        """
        return self._native_name

    @native_name.setter
    def native_name(self, native_name):
        """Sets the native_name of this SubjectName.

        The full name expressed as in the native language.  # noqa: E501

        :param native_name: The native_name of this SubjectName.  # noqa: E501
        :type: str
        """

        self._native_name = native_name

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
        if issubclass(SubjectName, dict):
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
        if not isinstance(other, SubjectName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
