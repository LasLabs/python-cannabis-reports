# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import BaseModel


class Effect(BaseModel):
    """Represents an effect profile."""

    euphoria = properties.Float(
        'Euphoric effect.',
        default=0.0,
    )
    creativity = properties.Float(
        'Creativity effect',
        default=0.0,
    )
    calming = properties.Float(
        'Calming effect',
        default=0.0,
    )
    numbness = properties.Float(
        'Numbness effect',
        default=0.0,
    )
    appetite_gain = properties.Float(
        'Appetite gain effect',
        default=0.0,
    )
    dry_mouth = properties.Float(
        'Dry mouth effect',
        default=0.0,
    )
    anxiety = properties.Float(
        'Anxiety effect',
        default=0.0,
    )


class Flavor(BaseModel):
    """Represents a flavor profile."""

    fruity = properties.Float(
        'Fruity flavor',
        default=0.0,
    )
    spicy = properties.Float(
        'Spicy flavor',
        default=0.0,
    )
    earthy = properties.Float(
        'Earthy flavor',
        default=0.0,
    )
    sour = properties.Float(
        'Sour flavor',
        default=0.0,
    )
    sweet = properties.Float(
        'Sweet flavor',
        default=0.0,
    )
    pine = properties.Float(
        'Pine flavor',
        default=0.0,
    )


class EffectsFlavors(Effect, Flavor):
    """Represents a flavor and effect profile."""
