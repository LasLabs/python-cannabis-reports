# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import recorder
from .api_product import ApiProductAbstract

from ..models.strain import Strain


class TestApisStrains(ApiProductAbstract):
    """Tests the Strains API endpoint."""

    UID = 'VUJCJ4TYMG000000000000000'

    def setUp(self):
        super(TestApisStrains, self).setUp()
        self.endpoint = self.api.Strains

    @recorder.use_cassette()
    def test_apis_strains_list(self):
        """It should parse the response and return the proper object."""
        self._test_apis_objects_list(Strain)

    @recorder.use_cassette()
    def test_apis_strains_get(self):
        """It should return the proper singleton."""
        self._test_apis_objects_get('Jack Herer')

    @recorder.use_cassette()
    def test_apis_strains_get_user(self):
        """It should return the proper user singleton."""
        self._test_apis_objects_get_user('David')

    @recorder.use_cassette()
    def test_apis_strains_get_review(self):
        """It should return the reviews."""
        self._test_apis_objects_get_review()

    @recorder.use_cassette()
    def test_apis_strains_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        self._test_apis_objects_get_effects_flavors()

    @recorder.use_cassette()
    def test_apis_strains_get_available(self):
        """It should return the menu items."""
        self._test_apis_objects_get_available()

    @recorder.use_cassette()
    def test_apis_strains_search(self):
        """It should parse the response and return the proper objects."""
        self._test_apis_objects_search('Blue', Strain)

    @recorder.use_cassette()
    def test_apis_strains_get_seed_company(self):
        """It should return the seed company."""
        seed_company = self.api.Strains.get_seed_company(
            'VUJCJ4TYMG000000000000000',
        )
        self.assertEqual(seed_company.name, 'Sensi Seeds')

    @recorder.use_cassette()
    def test_apis_strains_get_genetics(self):
        """It should return the parent strains."""
        genetics = self.api.Strains.get_genetics('CYGU94JYKY000000000000000')
        found_parent = False
        for genetic in genetics:
            self.assertIsInstance(genetic, Strain)
            if genetic.name == 'Afghani No. 1':
                found_parent = True
        self.assertTrue(found_parent)

    @recorder.use_cassette()
    def test_apis_strains_get_children(self):
        """It should return the child strains."""
        children = self.api.Strains.get_children('VUJCJ4TYMG000000000000000',
                                                 limit=self.LIMIT_PAGE)
        found_child = False
        for child in children:
            self.assertIsInstance(child, Strain)
            if child.name == 'Jack Flash':
                found_child = True
        self.assertTrue(found_child)
