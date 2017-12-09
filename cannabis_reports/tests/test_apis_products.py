# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_product import ApiProductAbstract

from ..models.product import Product


class TestApisProducts(ApiProductAbstract):
    """Tests the Products API endpoint."""

    UID = '9XVU7NK3PEGLAJ372X4F00000'

    def setUp(self):
        super(TestApisProducts, self).setUp()
        self.endpoint = self.api.Products

    @recorder.use_cassette()
    def test_apis_products_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Product)

    @recorder.use_cassette()
    def test_apis_products_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Cherry Kola - Pre-roll')

    @recorder.use_cassette()
    def test_apis_products_get_user(self):
        """It should return the proper user singleton."""
        self._test_apis_objects_get_user('Shelly')

    @recorder.use_cassette()
    def test_apis_products_get_review(self):
        """It should return the reviews."""
        self.UID = '0000000000C6FZLK664400000'
        self._test_apis_objects_get_review()

    @recorder.use_cassette()
    def test_apis_products_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        self.UID = '0000000000C6FZLK664400000'
        self._test_apis_objects_get_effects_flavors('numbness')

    @recorder.use_cassette()
    def test_apis_products_get_available(self):
        """It should return the menu items."""
        self.UID = '0000000000C6FZLK664400000'
        self._test_apis_objects_get_available()

    @recorder.use_cassette()
    def test_apis_products_search(self):
        """It should parse the response and return the proper objects."""
        self._test_apis_objects_search('pre-roll', Product)

    @recorder.use_cassette()
    def test_apis_products_get_producer(self):
        """It should return the producer."""
        self._test_apis_objects_get_producer('Emeralds')

    @recorder.use_cassette()
    def test_apis_products_get_strain(self):
        """It should return the strain."""
        self._test_apis_objects_get_strain('Cherry Kola')
