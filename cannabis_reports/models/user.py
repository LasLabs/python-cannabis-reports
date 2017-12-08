# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import BaseModelWithLinks


class User(BaseModelWithLinks):
    """Represents a CannabisReports user."""

    nickname = properties.String(
        'The user nickname.',
    )
    tagline = properties.String(
        'The user tagline.',
    )
    slug = properties.String(
        'The user slug.',
    )
