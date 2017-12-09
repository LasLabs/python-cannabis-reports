# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .. import BaseApi

from ..exceptions import CannabisReportsValidationException

from ..models.edible import Edible
from ..models.extract import Extract
from ..models.menu_item import MenuItemSummary
from ..models.product import Product


class AbstractEntityEndpoint(BaseApi):
    """This represents an abstract entity endpoint.

    The Dispensaries and Producers API inherit from this.
    """

    @classmethod
    def get_extracts(cls, session, ucpc, path_prefix=None, limit=None):
        """Gets a paginated list of extracts for a producer with the
        given UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis producer you want the extracts for.
            path_prefix (str, optional): A URI path to prefix with, which
                is useful for dispensary hierarchies. This will override
                the endpoint prefix, so it should include it if necessary.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=Extract):
                The extracts for this producer.
        """
        return cls(
            '/%s/%s/extracts' % (path_prefix or cls.__endpoint__, ucpc),
            session=session,
            out_type=Extract,
            iteration_limit=limit,
        )

    @classmethod
    def get_edibles(cls, session, ucpc, path_prefix=None, limit=None):
        """Gets a paginated list of edibles for a producer with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis producer you want the edibles for.
            path_prefix (str, optional): A URI path to prefix with, which
                is useful for dispensary hierarchies. This will override
                the endpoint prefix, so it should include it if necessary.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=Edible):
                The edibles for this producer.
        """
        return cls(
            '/%s/%s/edibles' % (path_prefix or cls.__endpoint__, ucpc),
            session=session,
            out_type=Edible,
            iteration_limit=None,
        )

    @classmethod
    def get_products(cls, session, ucpc, path_prefix=None, limit=None):
        """Gets a paginated list of products for a producer with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis producer you want the products for.
            path_prefix (str, optional): A URI path to prefix with, which
                is useful for dispensary hierarchies. This will override
                the endpoint prefix, so it should include it if necessary.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=Product):
                The products for this producer.
        """
        return cls(
            '/%s/%s/products' % (path_prefix or cls.__endpoint__, ucpc),
            session=session,
            out_type=Product,
            iteration_limit=None,
        )

    @classmethod
    def get_available(cls, session, ucpc, lat, lng, radius=10,
                      path_prefix=None, limit=None):
        """Get information about the availability of everything from a
        producer using latitude and longitude.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want the children from.
            lat (float): Latitude for the center of your availability search.
            lng (float): Longitude for the center of your availability search.
            radius (int): Radius to search for in miles, max 25.
            path_prefix (str, optional): A URI path to prefix with, which
                is useful for dispensary hierarchies. This will override
                the endpoint prefix, so it should include it if necessary.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=cls.__object__):
                An iterator of child objects.
        """
        if radius > 25:
            raise CannabisReportsValidationException(
                'The max search radius is 25.',
            )
        return cls(
            '/%s/%s/availability/geo/%s/%s/%s' % (
                path_prefix or cls.__endpoint__, ucpc, lat, lng, radius,
            ),
            session=session,
            out_type=MenuItemSummary,
            iteration_limit=limit,
        )
