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

    def setUp(self):
        super(ApiCommon, self).setUp()
        self.api = CannabisReports()
