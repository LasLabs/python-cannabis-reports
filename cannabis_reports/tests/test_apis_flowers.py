# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_product import ApiProductAbstract

from ..models.flower import Flower


class TestApisFlowers(ApiProductAbstract):
    """Tests the Flowers API endpoint."""

    UID = 'AHZ7H4N6467FVUDY3DAY00000'

    def setUp(self):
        super(TestApisFlowers, self).setUp()
        self.endpoint = self.api.Flowers

    @recorder.use_cassette()
    def test_apis_flowers_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Flower)

    @recorder.use_cassette()
    def test_apis_flowers_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Ogre Berry - Flowers')

    @recorder.use_cassette()
    def test_apis_flowers_get_user(self):
        """It should return the proper user singleton."""
        self._test_apis_objects_get_user('jbcrockett')

    @recorder.use_cassette()
    def test_apis_flowers_get_review(self):
        """It should return the reviews."""
        self._test_apis_objects_get_review()

    @recorder.use_cassette()
    def test_apis_flowers_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        self._test_apis_objects_get_effects_flavors()

    @recorder.use_cassette()
    def test_apis_flowers_get_available(self):
        """It should return the menu items."""
        self.UID = 'YYRZDWGVU22WJVPGDJ7J00000'
        self._test_apis_objects_get_available()

    @recorder.use_cassette()
    def test_apis_flowers_search(self):
        """It should parse the response and return the proper objects."""
        self._test_apis_objects_search('flowers', Flower)

    @recorder.use_cassette()
    def test_apis_flowers_get_producer(self):
        """It should return the producer."""
        self._test_apis_objects_get_producer('HappyDay Farms')

    @recorder.use_cassette()
    def test_apis_flowers_get_strain(self):
        """It should return the strain."""
        self._test_apis_objects_get_strain('Ogre Berry')
