# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_product_endpoint import AbstractProductEndpoint

from ..models.product import Product


class Products(AbstractProductEndpoint):
    """This represents the ``Products`` Endpoint.

    https://developers.cannabisreports.com/docs/products
    """

    __object__ = Product
    __endpoint__ = 'products'
