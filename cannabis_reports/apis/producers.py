# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .. import BaseApi

from ..exceptions import CannabisReportsValidationException

from ..models.edible import Edible
from ..models.extract import Extract
from ..models.menu_item import MenuItemSummary
from ..models.producer import Producer
from ..models.product import Product


class Producers(BaseApi):
    """This represents the ``Producers`` Endpoint.

    https://developers.cannabisreports.com/docs/producers
    """

    __object__ = Producer
    __endpoint__ = 'producers'

    @classmethod
    def get_extracts(cls, session, ucpc):
        """Gets a paginated list of extracts for a producer with the
        given UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis producer you want the extracts for.

        Returns:
            RequestPaginator(output_type=Extract):
                The extracts for this producer.
        """
        return cls(
            '/%s/%s/extracts' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Extract,
        )

    @classmethod
    def get_edibles(cls, session, ucpc):
        """Gets a paginated list of edibles for a producer with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis producer you want the edibles for.

        Returns:
            RequestPaginator(output_type=Edible):
                The edibles for this producer.
        """
        return cls(
            '/%s/%s/edibles' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Edible,
        )

    @classmethod
    def get_products(cls, session, ucpc):
        """Gets a paginated list of products for a producer with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis producer you want the products for.

        Returns:
            RequestPaginator(output_type=Product):
                The products for this producer.
        """
        return cls(
            '/%s/%s/products' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Product,
        )

    @classmethod
    def get_available(cls, session, ucpc, lat, lng, radius=10):
        """Get information about the availability of everything from a
        producer using latitude and longitude.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis object you want the children from.
            lat (float): Latitude for the center of your availability search.
            lng (float): Longitude for the center of your availability search.
            radius (int): Radius to search for in miles, max 25.

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
                cls.__endpoint__, ucpc, lat, lng, radius,
            ),
            session=session,
            out_type=MenuItemSummary,
        )
