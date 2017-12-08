# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import requests

from ..exceptions import CannabisReportsRemoteException


class RequestPaginator(object):
    """ RequestPaginator provides an iterator based upon an initial request.
    """

    # Response attributes that mean things
    PAGE_TOTAL = 'total_pages'  # Total number of pages
    PAGE_CURRENT = 'current_page'  # Current page number
    PAGE_DATA = 'data'  # Attribute if multiple results

    SSL_VERIFY = True  # Verify SSL

    # HTTP operation constants
    DELETE = 'delete'
    GET = 'get'
    POST = 'post'
    PUT = 'put'

    # Starting page ints
    page_current = 0
    page_total = 0

    def __init__(self, endpoint, data=None, output_type=dict,
                 request_type=GET, session=None, iteration_limit=None):
        """Initialize the RequestPaginator object.

        Args:
            endpoint (str): URI endpoint to call.
            session (requests.Session): The authenticated requests session.
            data (dict, optional): Data to be sent in the query string for
                the Request.
            output_type (type, optional): Class type to output. Object will be
                instantiated using the current row before output.
            request_type (str, optional): Type of request to send (``GET`` or
                ``POST``).
            session (requests.Session, optional): An authenticated requests
                session to use.
            iteration_limit (int, optional): Stop after iterating this many
                pages.

        Raises:
            NotImplementedError: In the event that an invalid request type was
             defined.
        """

        if request_type not in (self.GET, self.POST, self.PUT, self.DELETE):
            raise NotImplementedError(
                'The `%s` request type is not implemented', request_type,
            )

        self.endpoint = endpoint
        self.data = data
        self.output_type = output_type
        self.request_type = request_type
        self.session = session or requests.Session()
        self.limit_iter = iteration_limit

    def __iter__(self, start_page=1):
        """Provide an iterator for the remote request.

        The result is returned as an instantiated `self.output_type`.

        Args:
            start_page (int, optional): The page number to start on.

        Raises:
            StopIteration: To indicate the end of the data set.

        Yields:
            mixed: An instantiated object of the type declared in the
                ``self.output_type``, using the data from each row of the
                received data.
        """

        self.page_current = start_page - 1
        self.page_total = start_page

        while self.page_current < self.page_total:

            data = self.data and self.data.copy() or None
            result = self.call(data)
            for row in result:
                yield self.output_type(**row)

            iteration_count = (self.page_current + 1) - start_page
            if self.limit_iter and iteration_count >= self.limit_iter:
                break

        raise StopIteration()

    def call(self, data=None):
        """Generic API caller. Return the JSON decoded result.

        Args:
            data (dict, optional): Either the request parameters or the JSON
             data, depending on the request type.

        Returns:
            mixed: JSON decoded response.
        """
        if data is None:
            data = {}
        data['page'] = self.page_current + 1
        return getattr(self, self.request_type)(data)

    def delete(self, json=None):
        """Send a DELETE request and return the JSON decoded result.

        Args:
            json (dict, optional): Object to encode and send in request.

        Returns:
            mixed: JSON decoded response data.
        """
        return self._call('delete', url=self.endpoint, json=json)

    def get(self, params=None):
        """Send a POST request and return the JSON decoded result.

        Args:
            params (dict, optional): Mapping of parameters to send in request.

        Returns:
            mixed: JSON decoded response data.
        """
        return self._call('get', url=self.endpoint, params=params)

    def post(self, json=None):
        """Send a POST request and return the JSON decoded result.

        Args:
            json (dict, optional): Object to encode and send in request.

        Returns:
            mixed: JSON decoded response data.
        """
        return self._call('post', url=self.endpoint, json=json)

    def put(self, json=None):
        """Send a PUT request and return the JSON decoded result.

        Args:
            json (dict, optional): Object to encode and send in request.

        Returns:
            mixed: JSON decoded response data.
        """
        return self._call('put', url=self.endpoint, json=json)

    def _call(self, method, *args, **kwargs):
        """Call the remote service and return the response data."""

        assert self.session

        method = getattr(self.session, method)

        if not kwargs.get('verify'):
            kwargs['verify'] = self.SSL_VERIFY

        return self._handle_response(
            method(*args, **kwargs),
        )

    def _handle_response(self, response):
        """Parse the response and return the result."""

        response_json = response.json()

        if response.status_code < 200 or response.status_code >= 300:
            message = response_json.get('error', response_json.get('message'))
            raise CannabisReportsRemoteException(response.status_code, message)

        pagination = response_json.get('meta', {}).get('pagination')
        if pagination:
            self.page_current = pagination.get(self.PAGE_CURRENT, 1)
            self.page_total = pagination.get(self.PAGE_TOTAL, 1)
        else:
            # Single page.
            self.page_current = 1
            self.page_total = 1

        try:
            return response_json[self.PAGE_DATA]
        except KeyError:
            pass

        # No data was received, but the request was still a success.
        return True
