# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..base_model import BaseModelWithLinks

from .effects_flavors import EffectsFlavors


class Review(BaseModelWithLinks, EffectsFlavors):
    """Represents a CannabisReports review."""
