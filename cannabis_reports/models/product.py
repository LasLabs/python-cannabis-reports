# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .producer import Producer
from .strain import Strain


class Product(LinksModelWithImage):
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

    name = properties.String(
        'Name of the product.',
    )
    barcode = properties.String(
        'Link to the barcode for this product.',
    )
    producer = properties.Instance(
        'Information about the producer that created the product.',
        instance_class=Producer,
    )
    type = properties.String(
        'Type of product.',
    )
    strain = properties.Instance(
        'Strain that this product comes from.',
        instance_class=Strain,
    )
    lab_test = properties.String(
        'Link to the PDF containing lab test information for this product.',
    )
    thc = properties.String(
        'Milligrams of `THC <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-thc-tetrahydrocannabinol>`_ in this '
        'product.',
    )
    cbd = properties.String(
        'Milligrams of `CBD <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-cbd-cannabidiol>`_ in this product.',
    )
    cannabis = properties.String(
        'Milligrams of cannabis in this product.',
    )
    hash_oil = properties.String(
        'Milligrams of hash oil in this product.',
    )
    reviews = properties.Instance(
        'Object containing information on the reviews for the product.',
        instance_class=GeneralOverview,
    )
