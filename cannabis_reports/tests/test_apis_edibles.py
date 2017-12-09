# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_product import ApiProductAbstract

from ..models.edible import Edible


class TestApisEdibles(ApiProductAbstract):
    """Tests the Edibles API endpoint."""

    UID = '4KXM32V9YFC3G2EUNWP400000'

    def setUp(self):
        super(TestApisEdibles, self).setUp()
        self.endpoint = self.api.Edibles

    @recorder.use_cassette()
    def test_apis_edibles_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Edible)

    @recorder.use_cassette()
    def test_apis_edibles_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Soda - Girl Scout Cookies and Cream')

    @recorder.use_cassette()
    def test_apis_edibles_get_user(self):
        """It should return the proper user singleton."""
        self._test_apis_objects_get_user('Untamed Dame')

    @recorder.use_cassette()
    def test_apis_edibles_get_review(self):
        """It should return the reviews."""
        self.UID = '0000000000L6M7ENLJVX00000'
        self._test_apis_objects_get_review()

    @recorder.use_cassette()
    def test_apis_edibles_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        self.UID = '0000000000L6M7ENLJVX00000'
        self._test_apis_objects_get_effects_flavors()

    @recorder.use_cassette()
    def test_apis_edibles_get_available(self):
        """It should return the menu items."""
        self.UID = '0000000000L6M7ENLJVX00000'
        self._test_apis_objects_get_available()

    @recorder.use_cassette()
    def test_apis_edibles_search(self):
        """It should parse the response and return the proper objects."""
        self._test_apis_objects_search('chocolate', Edible)

    @recorder.use_cassette()
    def test_apis_edibles_get_producer(self):
        """It should return the producer."""
        self._test_apis_objects_get_producer('Kushtown')

    @recorder.use_cassette()
    def test_apis_edibles_get_strain(self):
        """It should return the strain."""
        self._test_apis_objects_get_strain('Girl Scout Cookies')
