# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item import AbstractItem


class Flower(AbstractItem):
    """Cannabis flowers are distinct products that can be found on retailer
    menus.

    The Cannabis Reports system allows for specific batches of cannabis
    flowers to be linked directly to the cultivator that grew the plant,
    while still maintaining a connection to the original genetics of the
    strain.

    Designating flowers as distinct items improves our ability to discuss
    the variety of flower quality that can be produced from the same strain
    grown at different farms.

    The main forms of flowers that Cannabis Reports recognizes are:

    * `Flowers <https://www.cannabisreports.com/flower-reports/flowers>`_
    * `Seeds <https://www.cannabisreports.com/flower-reports/seeds>`_
    * `Clones <https://www.cannabisreports.com/flower-reports/clones>`_
    * `Shake <https://www.cannabisreports.com/flower-reports/shake>`_

    Producers measure the cannabinoid content of their flowers in many ways.
    Currently, Cannabis Reports allows producers to display the percentage
    of weight for THC and CBD.
    """
