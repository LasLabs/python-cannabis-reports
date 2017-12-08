# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import GeneralOverview, LineageModel


class SeedCompany(LineageModel):
    """Cannabis seed companies create the variety of strains available for
    growing and breeding.
    """

    name = properties.String(
        'The name of this seed company.',
    )
    strains = properties.Instance(
        'Object containing information on the strains available from this '
        'seed company.',
        instance_class=GeneralOverview,
    )
    reviews = properties.Instance(
        'The number of reviews for all of the strains available from this '
        'seed company.',
        instance_class=GeneralOverview,
    )
