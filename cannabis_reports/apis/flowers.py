# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_product_endpoint import AbstractProductEndpoint

from ..models.flower import Flower


class Flowers(AbstractProductEndpoint):
    """This represents the ``Flowers`` Endpoint.

    https://developers.cannabisreports.com/docs/flowers
    """

    __object__ = Flower
    __endpoint__ = 'flowers'
