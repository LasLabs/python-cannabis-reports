# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LinksModelWithImage


class Producer(LinksModelWithImage):
    """Cannabis producers are the ones that create all of the cannabis flowers,
    extracts, edibles, and other products we know and love.

    More information about cannabis producers can be found in the `Cannabis
    Reports FAQ <https://www.cannabisreports.com/faq/cannabis-community/
    what-is-a-cannabis-producer>`_.
    """

    reviews = properties.Instance(
        'The number of reviews for all of the strains available from this '
        'seed Producer.',
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
