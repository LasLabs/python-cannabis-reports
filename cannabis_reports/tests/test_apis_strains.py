# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import ApiCommon, recorder

from ..models.menu_item import MenuItemSummary
from ..models.strain import Strain
from ..models.review import Review


class TestApisStrains(ApiCommon):
    """Tests the Strains API endpoint."""

    @recorder.use_cassette()
    def test_apis_strains_list(self):
        """It should parse the response and return the proper object."""
        result_count = 0
        for strain in self.api.Strains.list(limit=self.LIMIT_PAGE):
            self.assertIsInstance(strain, Strain)
            result_count += 1
        self.assertEqual(result_count, self.LIMIT_LIST * self.LIMIT_PAGE)

    @recorder.use_cassette()
    def test_apis_strains_get(self):
        """It should return the proper singleton."""
        strain = self.api.Strains.get('VUJCJ4TYMG000000000000000')
        self.assertEqual(strain.name, 'Jack Herer')

    @recorder.use_cassette()
    def test_apis_strains_get_user(self):
        """It should return the proper user singleton."""
        user = self.api.Strains.get_user('VUJCJ4TYMG000000000000000')
        self.assertEquals(user.nickname, 'David')

    @recorder.use_cassette()
    def test_apis_strains_get_review(self):
        """It should return the reviews."""
        reviews = self.api.Strains.get_reviews('VUJCJ4TYMG000000000000000')
        for review in reviews:
            self.assertIsInstance(review, Review)

    @recorder.use_cassette()
    def test_apis_strains_get_effects_flavors(self):
        """It should return the effect & flavor profile."""
        effect_flavor = self.api.Strains.get_effects_flavors(
            'VUJCJ4TYMG000000000000000',
        )
        self.assertGreater(effect_flavor.euphoria, 0)

    @recorder.use_cassette()
    def test_apis_strains_get_available(self):
        """It should return the menu items."""
        available = self.api.Strains.get_available(
            'VUJCJ4TYMG000000000000000', 37.7749295, -122.4194155,
        )
        for available in available:
            self.assertIsInstance(available, MenuItemSummary)

    @recorder.use_cassette()
    def test_apis_strains_search(self):
        """It should parse the response and return the proper objects."""
        result_count = 0
        for strain in self.api.Strains.search('Blue', limit=self.LIMIT_PAGE):
            self.assertIsInstance(strain, Strain)
            result_count += 1
        self.assertEqual(result_count, self.LIMIT_LIST * self.LIMIT_PAGE)

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
