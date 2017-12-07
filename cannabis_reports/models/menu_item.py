# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties

from ..base_model import BaseModel

from .dispensary import Dispensary


class MenuItem(BaseModel):
    """Menu items for dispensaries."""

    name = properties.String(
        'Name of the item.',
    )
    type = properties.StringChoice(
        'Type of item.',
        choices=['strain', 'extract', 'edible', 'product'],
    )
    item = properties.Property(
        'The strain, extract, edible, or product.',
    )
    price = properties.Float(
        'The price for the item. This is not set for strains and extracts.',
    )
    price_half_gram = properties.Float(
        'Price for one half gram of the item. This is not set for edibles '
        'and products.',
    )
    price_gram = properties.Float(
        'Price for one gram of this item. This is not set for edibles and '
        'products.',
    )
    price_eighth = properties.Float(
        'Price for one eighth ounce of this item. This is not set for '
        'edibles and products.',
    )
    price_quarter = properties.Float(
        'Price for one quarter ounce of this item. This is not set for '
        'edibles and products.',
    )
    price_half_ounce = properties.Float(
        'Price for one half ounce of this item. This is not set for '
        'edibles and products.',
    )
    price_ounce = properties.Float(
        'Price for one ounce of this item. This is not set for '
        'edibles and products.',
    )


class MenuItemSummary(MenuItem):
    """Menu item summary for when it is known what the menu item is."""

    location = properties.Instance(
        'Object containing information about the location this item is at.',
        instance_class=Dispensary,
    )
