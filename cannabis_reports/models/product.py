# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item import AbstractItem


class Product(AbstractItem):
    """Cannabis products cover a wide variety of additional products that
    contain cannabis.

    Anything that wouldn't be consumed like an product or extract falls into
    this category. Pre-rolled cannabis is also in this category.

    The main forms of products that Cannabis Reports recognizes are:

    * `Bath <https://www.cannabisreports.com/product-reports/bath>`_
    * `Topical <https://www.cannabisreports.com/product-reports/topical>`_
    * `Skin Care <https://www.cannabisreports.com/product-reports/skin-care>`_
    * `Pre-Roll <https://www.cannabisreports.com/product-reports/pre-roll>`_

    Cannabis Reports also supports "Other" types of products. Some examples
    are:

    * Lip Balm
    * Massage Oil
    * Personal Lubricant

    Producers measure the amount of cannabis in their products in a variety of
    ways. We recognize 4 ways for measuring the cannabis contents:

    * THC mg
    * CBD mg
    * Cannabis mg
    * Hash Oil mg

    More information about cannabis products can be found in the `FAQ
    <https://www.cannabisreports.com/faq/typesconsumption/
    what-is-a-cannabis-product>`_.
    """
