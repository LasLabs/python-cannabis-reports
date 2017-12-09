# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_product_endpoint import AbstractProductEndpoint

from ..models.extract import Extract


class Extracts(AbstractProductEndpoint):
    """This represents the ``Extracts`` Endpoint.

    https://developers.cannabisreports.com/docs/extracts
    """

    __object__ = Extract
    __endpoint__ = 'extracts'
