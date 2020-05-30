# coding: utf-8

"""
    Order Details

    Retrieve information about current and past orders.  # noqa: E501

    OpenAPI spec version: v3
    Contact: api.contact@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import digikey.v3.ordersupport
from digikey.v3.ordersupport.api.order_details_api import OrderDetailsApi  # noqa: E501
from digikey.v3.ordersupport.rest import ApiException


class TestOrderDetailsApi(unittest.TestCase):
    """OrderDetailsApi unit test stubs"""

    def setUp(self):
        self.api = digikey.v3.ordersupport.api.order_details_api.OrderDetailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_history_get(self):
        """Test case for history_get

        Retrieves a list of SalesorderIds and dates for all Salesorders within a date range belonging to a CustomerId.  # noqa: E501
        """
        pass

    def test_status_salesorder_id_get(self):
        """Test case for status_salesorder_id_get

        Retrieve order status for given SalesorderId  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()