# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .api_common import ApiCommon

from ..models.menu_item import MenuItemSummary
from ..models.review import Review


class ApiProductAbstract(ApiCommon):
    """Tests the AbstractProductEndpoint API endpoints."""

    def _test_apis_objects_get_user(self, expect_name):
        """It should return the proper user singleton."""
        user = self.endpoint.get_user(self.UID)
        self.assertEquals(user.nickname, expect_name)

    def _test_apis_objects_get_review(self):
        """It should return the reviews."""
        reviews = self.endpoint.get_reviews(self.UID)
        got_results = False
        for review in reviews:
            self.assertIsInstance(review, Review)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_get_effects_flavors(self, attribute='euphoria'):
        """It should return the effect & flavor profile."""
        effect_flavor = self.endpoint.get_effects_flavors(self.UID)
        self.assertGreater(getattr(effect_flavor, attribute), 0)

    def _test_apis_objects_get_available(self):
        """It should return the menu items."""
        available = self.endpoint.get_available(
            self.UID, 37.7749295, -122.4194155,
        )
        got_results = False
        for available in available:
            self.assertIsInstance(available, MenuItemSummary)
            got_results = True
        self.assertTrue(got_results)

    def _test_apis_objects_search(self, query, expect_class):
        """It should parse the response and return the proper objects."""
        result_count = 0
        results = self.endpoint.search(query, limit=self.LIMIT_PAGE)
        for result in results:
            self.assertIsInstance(result, expect_class)
            result_count += 1
        self.assertEqual(result_count, self.LIMIT_LIST * self.LIMIT_PAGE)

    def _test_apis_objects_get_producer(self, expect_name):
        """It should return the producer."""
        producer = self.endpoint.get_producer(self.UID)
        self.assertEqual(producer.name, expect_name)

    def _test_apis_objects_get_strain(self, expect_name):
        """It should return the strain."""
        strain = self.endpoint.get_strain(self.UID)
        self.assertEqual(strain.name, expect_name)
