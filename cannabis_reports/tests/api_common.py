# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from os.path import dirname, join

from vcr import VCR

from .. import CannabisReports


recorder = VCR(
    record_mode='once',
    cassette_library_dir=join(dirname(__file__), 'fixtures/cassettes'),
    path_transformer=VCR.ensure_suffix('.yml'),
    filter_headers=['X-API-Key'],
)


class ApiCommon(unittest.TestCase):

    LIMIT_LIST = 10
    LIMIT_PAGE = 2

    # Subclasses must define this, such as ``self.api.Edibles``
    endpoint = None
    # Subclasses must define this, typically a UCPC
    UID = None

    def setUp(self):
        super(ApiCommon, self).setUp()
        self.api = CannabisReports()

    def _test_apis_objects_list(self, expect_class):
        """It should parse the response and return the proper object."""
        result_count = 0
        for result in self.endpoint.list(limit=self.LIMIT_PAGE):
            self.assertIsInstance(result, expect_class)
            result_count += 1
        self.assertEqual(result_count, self.LIMIT_LIST * self.LIMIT_PAGE)

    def _test_apis_objects_get(self, expect_name):
        """It should return the proper singleton."""
        result = self.endpoint.get(self.UID)
        self.assertEqual(result.name, expect_name)
