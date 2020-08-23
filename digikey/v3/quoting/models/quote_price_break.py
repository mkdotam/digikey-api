# coding: utf-8

"""
    Quoting Api

    Create/Update/Read for Quoting  # noqa: E501

    OpenAPI spec version: v3
    Contact: api.support@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class QuotePriceBreak(object):
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
        'break_quantity': 'int',
        'total_price': 'float',
        'unit_price': 'float'
    }

    attribute_map = {
        'break_quantity': 'BreakQuantity',
        'total_price': 'TotalPrice',
        'unit_price': 'UnitPrice'
    }

    def __init__(self, break_quantity=None, total_price=None, unit_price=None):  # noqa: E501
        """QuotePriceBreak - a model defined in Swagger"""  # noqa: E501

        self._break_quantity = None
        self._total_price = None
        self._unit_price = None
        self.discriminator = None

        if break_quantity is not None:
            self.break_quantity = break_quantity
        if total_price is not None:
            self.total_price = total_price
        if unit_price is not None:
            self.unit_price = unit_price

    @property
    def break_quantity(self):
        """Gets the break_quantity of this QuotePriceBreak.  # noqa: E501


        :return: The break_quantity of this QuotePriceBreak.  # noqa: E501
        :rtype: int
        """
        return self._break_quantity

    @break_quantity.setter
    def break_quantity(self, break_quantity):
        """Sets the break_quantity of this QuotePriceBreak.


        :param break_quantity: The break_quantity of this QuotePriceBreak.  # noqa: E501
        :type: int
        """

        self._break_quantity = break_quantity

    @property
    def total_price(self):
        """Gets the total_price of this QuotePriceBreak.  # noqa: E501


        :return: The total_price of this QuotePriceBreak.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this QuotePriceBreak.


        :param total_price: The total_price of this QuotePriceBreak.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def unit_price(self):
        """Gets the unit_price of this QuotePriceBreak.  # noqa: E501


        :return: The unit_price of this QuotePriceBreak.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this QuotePriceBreak.


        :param unit_price: The unit_price of this QuotePriceBreak.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

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
        if issubclass(QuotePriceBreak, dict):
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
        if not isinstance(other, QuotePriceBreak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other