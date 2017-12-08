# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .producer import Producer
from .strain import Strain


class Extract(LinksModelWithImage):
    """Cannabis extracts are created from the flowers of the cannabis plant.

     Various methods for creating cannabis extracts have been perfected over
     thousands of years.

    Cannabis Reports recognizes 10 main types of extracts:

    * `Kief <https://www.cannabisreports.com/extract-reports/kief>`_
    * `Hash <https://www.cannabisreports.com/extract-reports/hash>`_
    * `Water-Hash <https://www.cannabisreports.com/extract-reports/
       water-hash>`_
    * `Oil <https://www.cannabisreports.com/extract-reports/oil>`_
    * `Wax <https://www.cannabisreports.com/extract-reports/wax>`_
    * `Crumble <https://www.cannabisreports.com/extract-reports/crumble>`_
    * `Honeycomb <https://www.cannabisreports.com/extract-reports/honeycomb>`_
    * `Shatter <https://www.cannabisreports.com/extract-reports/shatter>`_
    * `Vaporizer-Disposable <https://www.cannabisreports.com/extract-reports/
      vaporizer-disposable>`_
    * `Vaporizer-Cartridge <https://www.cannabisreports.com/extract-reports/
      vaporizer-cartridge>`_

    Each extract is tied to a strain and the producer who created it. For more
    information about cannabis extracts, check out the `FAQ
    <https://www.cannabisreports.com/faq/typesconsumption/
    what-is-a-cannabis-extract>`_
    """

    name = properties.String(
        'Name of the extract.',
    )
    barcode = properties.String(
        'Link to the barcode for this extract.',
    )
    producer = properties.Instance(
        'Information about the producer that created the extract.',
        instance_class=Producer,
    )
    type = properties.String(
        'Type of extract.',
    )
    strain = properties.Instance(
        'Strain that this extract comes from.',
        instance_class=Strain,
    )
    lab_test = properties.String(
        'Link to the PDF containing lab test information for this extract.',
    )
    thc = properties.String(
        'Percentage of `THC <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-thc-tetrahydrocannabinol>`_ in this '
        'extract.',
    )
    cbd = properties.String(
        'Percentage of `CBD <https://www.cannabisreports.com/faq/'
        'cannabis-community/what-is-cbd-cannabidiol>`_ in this extract.',
    )
    reviews = properties.Instance(
        'Object containing information on the reviews for the extract.',
        instance_class=GeneralOverview,
    )
