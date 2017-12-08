# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock
import unittest

from contextlib import contextmanager

from ..request_paginator import RequestPaginator


class TestRequestPaginator(unittest.TestCase):

    REQUEST_TYPES = ['get', 'delete', 'post', 'put']

    def setUp(self):
        self.vals = {
            'endpoint': 'endpoint',
            'data': {'param': 1},
            'output_type': dict,
        }
        self.test_responses = [
            {
                'meta': {
                    'pagination': {
                        'current_page': 1,
                        'total_pages': 3,
                    },
                },
                'data': [{
                    'page': 1,
                }],
            },
            {
                'meta': {
                    'pagination': {
                        'current_page': 2,
                        'total_pages': 3,
                    },
                },
                'data': [{
                    'page': 2,
                }],
            },
            {
                'meta': {
                    'pagination': {
                        'current_page': 3,
                        'total_pages': 3,
                    },
                },
                'data': [{
                    'page': 3,
                }],
            },
        ]
        self.paginator = RequestPaginator(**self.vals)

    @contextmanager
    def mock_session(self, response_code=200, responses=None,
                     mock_attrs=None):
        if responses is None:
            responses = self.test_responses
        if mock_attrs is None:
            mock_attrs = ['get', 'delete', 'post', 'put']
        elif isinstance(mock_attrs, str):
            mock_attrs = [mock_attrs]
        with mock.patch.object(self.paginator, 'session') as session:
            response = mock.MagicMock()
            response.status_code = response_code
            response.json.side_effect = responses
            for attr in mock_attrs:
                method = getattr(session, attr)
                method.return_value = response
            yield session

    def do_call(self, request_type='get'):
        self.params = {'param_test': 23234}
        with self.mock_session(mock_attrs=request_type) as session:
            return session, getattr(self.paginator, request_type)(self.params)

    def _test_result(self, res):
        self.assertEqual(len(res), 1)
        self.assertDictEqual(res[0], self.test_responses[0]['data'][0])

    def _test_session_call_json(self, session, request_type):
        method = getattr(session, request_type)
        method.assert_called_once_with(
            url=self.vals['endpoint'],
            json=self.params,
            verify=True,
        )

    def test_init_attrs(self):
        """ It should correctly assign instance attributes. """
        attrs = {
            attr: getattr(self.paginator, attr) for attr in self.vals.keys()
        }
        self.assertDictEqual(attrs, self.vals)

    @mock.patch('cannabis_reports.request_paginator.requests')
    def test_init_session(self, requests):
        """ It should initialize a requests session. """
        paginator = RequestPaginator(**self.vals)
        self.assertEqual(paginator.session, requests.Session())

    def test_get_gets(self):
        """ It should call the session with proper args. """
        session, _ = self.do_call()
        session.get.assert_called_once_with(
            url=self.vals['endpoint'],
            params=self.params,
            verify=True,
        )

    def test_returns(self):
        """The returns should all return properly."""
        for request_type in self.REQUEST_TYPES:
            _, res = self.do_call(request_type)
            self._test_result(res)

    def test_session_calls(self):
        """The calls should all be handled properly (tests all but GET)."""
        self.REQUEST_TYPES.remove('get')
        for request_type in self.REQUEST_TYPES:
            session, _ = self.do_call(request_type)
            self._test_session_call_json(session, request_type)

    def test_call_get(self):
        """It should get when the request type is GET."""
        params = {'param_test': 23234}
        self.paginator.request_type = self.paginator.GET
        with mock.patch.object(self.paginator, 'get') as get:
            self.paginator.call(params)
        get.assert_called_once_with(params)

    def test_call_post(self):
        """It should post when the request type is POST."""
        params = {'param_test': 23234}
        self.paginator.request_type = self.paginator.POST
        with mock.patch.object(self.paginator, 'post') as post:
            self.paginator.call(params)
        post.assert_called_once_with(params)

    def test_iter(self):
        """ It should iterate until the end & yield data. """
        with self.mock_session() as session:
            session.get().json.side_effect = self.test_responses
            res = list(self.paginator)
            expect = [{'page': 1}, {'page': 2}, {'page': 3}]
            self.assertEqual(res, expect)

    def test_iter_limit(self):
        """ It should stop iteration after the correct page. """
        with self.mock_session() as session:
            session.get().json.side_effect = self.test_responses
            self.paginator.limit_iter = 2
            res = list(self.paginator)
            expect = [{'page': 1}, {'page': 2}]
            self.assertEqual(res, expect)
