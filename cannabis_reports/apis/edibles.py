# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_product_endpoint import AbstractProductEndpoint

from ..models.edible import Edible


class Edibles(AbstractProductEndpoint):
    """This represents the ``Edibles`` Endpoint.

    https://developers.cannabisreports.com/docs/edibles
    """

    __object__ = Edible
    __endpoint__ = 'edibles'
