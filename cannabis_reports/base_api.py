# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .base_model import BaseModel
from .request_paginator import RequestPaginator


class BaseApi(object):
    """This is the API interface object to be implemented by API adapters.

    It acts as a collection for the API object that it represents, passing
    through iteration to the API's request paginator.

    Attributes:
        BASE_URI (str): CannabisReports API URI base.
        paginator (RequestPaginator): Object to use for producing an iterator
         representing multiple requests (API response pages). Created on init.
        __object__ (cannabis_reports.models.BaseModel): Model object that API
         represents.
    """

    BASE_URI = 'https://www.cannabisreports.com/api/v1.0'

    # This should be replaced in child classes with the correct model.
    __object__ = BaseModel

    # This should be replaced with the endpoint, such as ``strains``
    __endpoint__ = None

    # This is set within new, after the object has been created.
    paginator = None

    def __new__(cls, endpoint, data=None,
                request_type=RequestPaginator.GET, singleton=False,
                session=None, out_type=None, iteration_limit=None):
        """Create a new API object.

        Args:
            endpoint (str): The API endpoint that this represents.
                ``BASE_URI`` will be prepended, with no slashes added.
            data (dict, optional): Data to send with the request.
            request_type (str, optional): Type of request (``GET or ``POST``).
                Defaults to ``GET``.
            singleton (bool, optional): Set this to ``True`` to assert that
                there is not more than one result, and return the first result
                (or ``None`` if there is no result).
            session (requests.Session, optional): An authenticated requests
                session to use.
            out_type (BaseModel, optional): If set, this object will be used
                for the creation of the models, instead of the one set in
                ``cls.__object__``.
            iteration_limit (int, optional): Limit of pages that can be
                iterated.

        Raises:
            CannabisReportsRemoteException: If ``singleton`` is ``True``, but
                the remote API responds with more than one result.

        Returns:
            BaseApi: An instance of an API object, if ``singleton`` is
                ``False``.
            BaseModel: An instance of a Model, if ``singleton`` is
                ``True`` and there are results.
            None: If ``singleton`` is ``True`` and there are no results.
        """
        if out_type is None:
            out_type = cls.__object__
        paginator = RequestPaginator(
            endpoint='%s%s' % (cls.BASE_URI, endpoint),
            data=data,
            output_type=out_type.from_api,
            request_type=request_type,
            session=session,
            iteration_limit=iteration_limit,
        )
        if singleton:
            results = paginator.call(paginator.data)
            if not results:
                return None
            return out_type.from_api(**results)
        obj = super(BaseApi, cls).__new__(cls)
        obj.paginator = paginator
        return obj

    def __iter__(self):
        """Pass through iteration to the API response."""
        for row in self.paginator:
            yield row
        raise StopIteration()

    @classmethod
    def new_object(cls, data):
        """Return a new object of the correct type from the data.

        Args:
            data (dict): Data dictionary that should be converted to an
                object. It can use either camelCase keys or snake_case.

        Returns:
            BaseModel: A model of the type declared in ``cls.__object__``.
        """
        return cls.__object__.from_api(**data)

    # Universal endpoints

    @classmethod
    def list(cls, session, sort='created_at', descending=False, limit=None):
        """Return all objects, with optional sorting.

        Args:
            session (requests.sessions.Session): Authenticated session.
            sort (str): Column to sort by. One of:

                * ``created_at``
                * ``updated_at``
                * ``name``

            descending (bool, optional): Set to True to put newest records
                at the top.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=cls.__object__):
                Objects iterator.
        """
        sort = BaseModel._to_camel_case(sort)
        if descending:
            sort = '-%s' % sort
        return cls(
            '/%s' % cls.__endpoint__,
            data={'sort': sort},
            session=session,
            iteration_limit=limit,
        )

    @classmethod
    def get(cls, session, ucpc):
        """Gets an individual object based on the UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want information about.

        Returns:
            cls.__object__: The object that was found.
        """
        return cls(
            '/%s/%s' % (cls.__endpoint__, ucpc),
            session=session,
            singleton=True,
        )
