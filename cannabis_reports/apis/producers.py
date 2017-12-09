# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..models.producer import Producer

from .abstract_entity_endpoint import AbstractEntityEndpoint


class Producers(AbstractEntityEndpoint):
    """This represents the ``Producers`` Endpoint.

    https://developers.cannabisreports.com/docs/producers
    """

    __object__ = Producer
    __endpoint__ = 'producers'
