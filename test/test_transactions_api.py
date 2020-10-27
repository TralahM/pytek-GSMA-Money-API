# coding: utf-8

"""
    Mobile Money API

    This document defines the RESTful endpoints provided by the GSMA Mobile Money API You can find out more about what the API can do for your business at [https://developer.mobilemoneyapi.io]   # noqa: E501

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.transactions_api import TransactionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batchtransactions_batch_id_completions_get(self):
        """Test case for batchtransactions_batch_id_completions_get

        View Batch Completions  # noqa: E501
        """
        pass

    def test_batchtransactions_batch_id_get(self):
        """Test case for batchtransactions_batch_id_get

        View A Transaction Batch  # noqa: E501
        """
        pass

    def test_batchtransactions_batch_id_patch(self):
        """Test case for batchtransactions_batch_id_patch

        Update A Transaction Batch  # noqa: E501
        """
        pass

    def test_batchtransactions_batch_id_rejections_get(self):
        """Test case for batchtransactions_batch_id_rejections_get

        View Batch Rejections  # noqa: E501
        """
        pass

    def test_batchtransactions_post(self):
        """Test case for batchtransactions_post

        Create A Transaction Batch  # noqa: E501
        """
        pass

    def test_transactions_post(self):
        """Test case for transactions_post

        Create a Transaction  # noqa: E501
        """
        pass

    def test_transactions_transaction_reference_get(self):
        """Test case for transactions_transaction_reference_get

        View A Transaction  # noqa: E501
        """
        pass

    def test_transactions_transaction_reference_reversals_post(self):
        """Test case for transactions_transaction_reference_reversals_post

        Create A Reversal  # noqa: E501
        """
        pass

    def test_transactionstypetransaction_type_put(self):
        """Test case for transactionstypetransaction_type_put

        Create a Transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()