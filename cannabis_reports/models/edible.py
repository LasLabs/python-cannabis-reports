# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .producer import Producer
from .strain import Strain


class Edible(LinksModelWithImage):
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

    name = properties.String(
        'Name of the edible.',
    )
    barcode = properties.String(
        'Link to the barcode for this edible.',
    )
    producer = properties.Instance(
        'Information about the producer that created the edible.',
        instance_class=Producer,
    )
    type = properties.String(
        'Type of edible.',
    )
    strain = properties.Instance(
        'Strain that this edible comes from.',
        instance_class=Strain,
    )
    lab_test = properties.String(
        'Link to the PDF containing lab test information for this edible.',
    )
    thc = properties.String(
        'Milligrams of `THC <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-thc-tetrahydrocannabinol>`_ in this '
        'edible.',
    )
    cbd = properties.String(
        'Milligrams of `CBD <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-cbd-cannabidiol>`_ in this edible.',
    )
    cannabis = properties.String(
        'Milligrams of cannabis in this edible.',
    )
    hash_oil = properties.String(
        'Milligrams of hash oil in this edible.',
    )
    reviews = properties.Instance(
        'Object containing information on the reviews for the edible.',
        instance_class=GeneralOverview,
    )
