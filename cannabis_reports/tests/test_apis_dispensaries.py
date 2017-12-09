# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_entity import ApiEntityAbstract

from ..models.dispensary import Dispensary


class TestApisDispensaries(ApiEntityAbstract):
    """Tests the Dispensaries API endpoint."""

    UID = 'ca/san-francisco/grass-roots'

    def setUp(self):
        super(TestApisDispensaries, self).setUp()
        self.endpoint = self.api.Dispensaries

    @recorder.use_cassette()
    def test_apis_dispensaries_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Dispensary)

    @recorder.use_cassette()
    def test_apis_dispensaries_get(self):
        """It should not be implemented."""
        self._test_apis_objects_get('Grass Roots')

    @recorder.use_cassette()
    def test_apis_dispensaries_get_extracts(self):
        """It should return the extracts for a dispensary."""
        self._test_apis_objects_get_extracts()

    @recorder.use_cassette()
    def test_apis_dispensaries_get_strains(self):
        """It should return the strains for a dispensary."""
        self._test_apis_objects_get_strains()

    @recorder.use_cassette()
    def test_apis_dispensaries_get_edibles(self):
        """It should return the edibles for a dispensary."""
        self._test_apis_objects_get_edibles()

    @recorder.use_cassette()
    def test_apis_dispensaries_get_products(self):
        """It should return the products for a dispensary."""
        self._test_apis_objects_get_products()

    @recorder.use_cassette()
    def test_apis_dispensaries_get_available(self):
        """It should not be implemented for this endpoint."""
        with self.assertRaises(NotImplementedError):
            self._test_apis_objects_get_available()
