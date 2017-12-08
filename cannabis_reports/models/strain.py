# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import BaseModel, GeneralOverview, LineageModel

from .seed_company import SeedCompany


class StrainGenetics(BaseModel):
    """Object that holds information about the genetics for the strain."""

    names = properties.String(
        'Genetics name. `More information <https://www.cannabisreports.com/'
        'faq/cannabis-genetics/how-do-you-read-cannabis-genetics>`_.',
    )
    link = properties.String(
        'Link to the genetic listing in the Cannabis Reports API.',
    )


class Strain(LineageModel):
    """Cannabis strains are the various cultivars available for the cannabis
    family. Thousands of years of human domestication and breeding of cannabis
    strains have resulted in a huge variety of attributes that we know and
    love today.

    `Wikipedia Definition <http://en.wikipedia.org/wiki/Cultivar>`_

    Over time, strain names have been used by various companies in their
    attempts to recreate the results of other breeders. Cannabis Reports
    identifies strains not only by their name, but by their seed company as
    well, to ensure they are all properly represented.
    """

    name = properties.String(
        'Name of the cannabis strain.',
    )
    seed_company = properties.Instance(
        'Information about the seed company that created or provides the '
        'strain.',
        instance_class=SeedCompany,
    )
    genetics = properties.Instance(
        'Object that holds information about the genetics for the strain.',
        instance_class=StrainGenetics,
    )
    children = properties.Instance(
        'Object that holds information about the children for the strain.',
        instance_class=GeneralOverview,
    )
    reviews = properties.Instance(
        'Object that holds information about the reviews for the strain.',
        instance_class=GeneralOverview,
    )
