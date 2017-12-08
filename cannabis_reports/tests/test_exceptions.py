# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..exceptions import (CannabisReportsRemoteException,
                          CannabisReportsValidationException,
                          )


class TestExceptions(unittest.TestCase):

    def test_cannabis_reports_remote_exception(self):
        """It should have the proper str representation."""
        code = 404
        message = 'A Fail'
        e = CannabisReportsRemoteException(code, message)
        self.assertEqual(str(e), '(404) A Fail')

    def test_cannabis_reports_base_exception(self):
        """It should include the message in string."""
        message = 'message'
        e = CannabisReportsValidationException(message)
        self.assertEqual(str(e), message)
