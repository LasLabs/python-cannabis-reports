# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import ApiCommon

from ..models.edible import Edible
from ..models.extract import Extract
from ..models.menu_item import MenuItemSummary
from ..models.product import Product
from ..models.strain import Strain


class ApiEntityAbstract(ApiCommon):
    """Tests the AbstractEntityEndpoint API endpoints."""

    def _test_apis_objects_get_extracts(self):
        extracts = self.endpoint.get_extracts(
            self.UID, limit=self.LIMIT_PAGE,
        )
        got_results = False
        for extract in extracts:
            self.assertIsInstance(extract, Extract)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_get_edibles(self):
        edibles = self.endpoint.get_edibles(
            self.UID, limit=self.LIMIT_PAGE,
        )
        got_results = False
        for edible in edibles:
            self.assertIsInstance(edible, Edible)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_get_products(self):
        products = self.endpoint.get_products(
            self.UID, limit=self.LIMIT_PAGE,
        )
        got_results = False
        for product in products:
            self.assertIsInstance(product, Product)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_get_strains(self):
        strains = self.endpoint.get_strains(
            self.UID, limit=self.LIMIT_PAGE,
        )
        got_results = False
        for strain in strains:
            self.assertIsInstance(strain, Strain)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_get_available(self):
        """It should return the menu items."""
        available = self.endpoint.get_available(
            self.UID, 37.7749295, -122.4194155, limit=self.LIMIT_PAGE,
        )
        got_results = False
        for available in available:
            self.assertIsInstance(available, MenuItemSummary)
            got_results = True
        self.assertTrue(got_results)
