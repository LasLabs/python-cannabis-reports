# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import BaseModel


class Address(BaseModel):
    """Object containing address location information."""

    address_1 = properties.String(
        'Street address.',
    )
    address_2 = properties.String(
        'Additional street address line.',
    )
    zip = properties.String(
        'Zip Code.',
    )
