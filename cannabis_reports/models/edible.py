# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item import AbstractItem


class Edible(AbstractItem):
    """Cannabis edibles cover a wide variety of consumable products that
    contain cannabis in various forms. From cotton candy, to tinctures,
    to dog treats, and everything in between.

    If it's a form of cannabis that is meant to be consumed, it is
    categorized as an edible.

    The main forms of edibles that Cannabis Reports recognizes are:

    * `Baked Goods <https://www.cannabisreports.com/edible-reports/
      baked-good>`_
    * `Candy <https://www.cannabisreports.com/edible-reports/candy>`_
    * `Treat <https://www.cannabisreports.com/edible-reports/treat>`_
    * `Chocolate <https://www.cannabisreports.com/edible-reports/chocolate>`_
    * `Snack <https://www.cannabisreports.com/edible-reports/snack>`_
    * `Beverage <https://www.cannabisreports.com/edible-reports/beverage>`_
    * `Pill <https://www.cannabisreports.com/edible-reports/pill>`_
    * `Tincture <https://www.cannabisreports.com/edible-reports/tincture>`_

    Cannabis Reports also supports "Other" types of edibles. Some examples
    are:

    * Butter
    * Honey
    * Breath Strips
    * Tea
    * Ice Cream

    Producers measure the amount of cannabis in their edibles in a variety of
    ways. We recognize 4 ways for measuring the cannabis contents:

    * THC mg
    * CBD mg
    * Cannabis mg
    * Hash Oil mg

    More information about cannabis edibles can be found in the `FAQ
    <https://www.cannabisreports.com/faq/typesconsumption/
    what-is-a-cannabis-edible>`_.
    """
