# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_product import ApiProductAbstract

from ..models.extract import Extract


class TestApisExtracts(ApiProductAbstract):
    """Tests the Extracts API endpoint."""

    UID = 'QLG39RN2AFPMR6WLTPLW00000'

    def setUp(self):
        super(TestApisExtracts, self).setUp()
        self.endpoint = self.api.Extracts

    @recorder.use_cassette()
    def test_apis_extracts_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Extract)

    @recorder.use_cassette()
    def test_apis_extracts_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Blackwater OG - Honeycomb')

    @recorder.use_cassette()
    def test_apis_extracts_get_user(self):
        """It should return the proper user singleton."""
        self._test_apis_objects_get_user('Untamed Dame')

    @recorder.use_cassette()
    def test_apis_extracts_get_review(self):
        """It should return the reviews."""
        self.UID = '9XVU762EQ4VU7TG3N9NM00000'
        self._test_apis_objects_get_review()

    @recorder.use_cassette()
    def test_apis_extracts_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        self.UID = '9XVU762EQ4VU7TG3N9NM00000'
        self._test_apis_objects_get_effects_flavors()

    @recorder.use_cassette()
    def test_apis_extracts_get_available(self):
        """It should return the menu items."""
        self.UID = '9XVU7ZCENQVU7TGRFHPC00000'
        self._test_apis_objects_get_available()

    @recorder.use_cassette()
    def test_apis_extracts_search(self):
        """It should parse the response and return the proper objects."""
        self._test_apis_objects_search('shatter', Extract)

    @recorder.use_cassette()
    def test_apis_extracts_get_producer(self):
        """It should return the producer."""
        self._test_apis_objects_get_producer('Jnetics')

    @recorder.use_cassette()
    def test_apis_extracts_get_strain(self):
        """It should return the strain."""
        self._test_apis_objects_get_strain('Blackwater OG')
