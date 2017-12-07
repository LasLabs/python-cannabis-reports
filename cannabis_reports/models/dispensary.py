# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage

from .address import Address


class Dispensary(LinksModelWithImage):
    """Cannabis producers are the ones that create all of the cannabis flowers,
    extracts, edibles, and other products we know and love.

    More information about cannabis producers can be found in the `Cannabis
    Reports FAQ <https://www.cannabisreports.com/faq/cannabis-community/
    what-is-a-cannabis-producer>`_.
    """

    name = properties.String(
        'Name of the dispensary.',
    )
    state = properties.String(
        'Two character representation of the state this dispensary is in.',
    )
    city = properties.String(
        'City this dispensary is in.',
    )
    lat = properties.String(
        'Latitude of this dispensary.',
    )
    lng = properties.String(
        'Longitude of this dispensary.',
    )
    address = properties.Instance(
        'Object containing additional location information for this '
        'dispensary.',
        instance_class=Address,
    )
    slug = properties.String(
        'Identifier for this dispensary; a combination of city and state.',
    )
    reviews = properties.Instance(
        'The number of reviews for all of the strains available from this '
        'seed Producer.',
        instance_class=GeneralOverview,
    )
    strains = properties.Instance(
        'Object containing information about strains available at this '
        'dispensary.',
        instance_class=GeneralOverview,
    )
    extracts = properties.Instance(
        'Information on all of the extracts that this producer makes.',
        instance_class=GeneralOverview,
    )
    edibles = properties.Instance(
        'Information on all of the edibles that this producer makes.',
        instance_class=GeneralOverview,
    )
    products = properties.Instance(
        'Information on all of the products that this producer makes.',
        instance_class=GeneralOverview,
    )
