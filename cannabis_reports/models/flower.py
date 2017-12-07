# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .producer import Producer
from .strain import Strain


class Flower(LinksModelWithImage):
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

    name = properties.String(
        'Name of the flower.',
    )
    barcode = properties.String(
        'Link to the barcode for this flower.',
    )
    producer = properties.Instance(
        'Information about the producer that created the flower.',
        instance_class=Producer,
    )
    type = properties.String(
        'Type of cannabis flower.',
    )
    strain = properties.Instance(
        'Strain that was used for this flower.',
        instance_class=Strain,
    )
    lab_test = properties.String(
        'Link to the PDF containing lab test information for this flower.',
    )
    thc = properties.String(
        'Percentage of `THC <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-thc-tetrahydrocannabinol>`_ in this '
        'flower.',
    )
    cbd = properties.String(
        'Percentage of `CBD <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-cbd-cannabidiol>`_ in this flower.',
    )
    reviews = properties.Instance(
        'Object containing information on the reviews for the flower.',
        instance_class=GeneralOverview,
    )
