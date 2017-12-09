# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .producer import Producer
from .strain import Strain


class AbstractItem(LinksModelWithImage):
    """Represents the base attributes for a saleable cannabis item."""

    name = properties.String(
        'Name of the item.',
    )
    barcode = properties.String(
        'Link to the barcode for this item.',
    )
    producer = properties.Instance(
        'Information about the producer that created the item.',
        instance_class=Producer,
    )
    type = properties.String(
        'Type of item.',
    )
    strain = properties.Instance(
        'Strain that this item comes from.',
        instance_class=Strain,
    )
    lab_test = properties.String(
        'Link to the PDF containing lab test information for this item.',
    )
    thc = properties.String(
        'Amount of `THC <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-thc-tetrahydrocannabinol>`_ in this '
        'item.',
    )
    cbd = properties.String(
        'Amount of `CBD <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-cbd-cannabidiol>`_ in this item.',
    )
    cannabis = properties.String(
        'Milligrams of cannabis in this item.',
    )
    hash_oil = properties.String(
        'Milligrams of hash oil in this item.',
    )
    reviews = properties.Instance(
        'Object containing information on the reviews for the item.',
        instance_class=GeneralOverview,
    )
