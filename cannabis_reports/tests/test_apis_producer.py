# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_entity import ApiEntityAbstract

from ..models.producer import Producer


class TestApisProducers(ApiEntityAbstract):
    """Tests the Producers API endpoint."""

    UID = '0000000000L6M7E0000000000'

    def setUp(self):
        super(TestApisProducers, self).setUp()
        self.endpoint = self.api.Producers

    @recorder.use_cassette()
    def test_apis_producers_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Producer)

    @recorder.use_cassette()
    def test_apis_producers_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Kiva')

    @recorder.use_cassette()
    def test_apis_producers_get_extracts(self):
        """It should return the extracts for a producer."""
        self.UID = '0000000000VU7TG0000000000'
        self._test_apis_objects_get_extracts()

    @recorder.use_cassette()
    def test_apis_producers_get_edibles(self):
        """It should return the edibles for a producer."""
        self._test_apis_objects_get_edibles()

    @recorder.use_cassette()
    def test_apis_producers_get_products(self):
        """It should return the products for a producer."""
        self.UID = '0000000000N4E9N0000000000'
        self._test_apis_objects_get_products()

    @recorder.use_cassette()
    def test_apis_producers_get_available(self):
        """It should return the availables for a producer."""
        self._test_apis_objects_get_available()
