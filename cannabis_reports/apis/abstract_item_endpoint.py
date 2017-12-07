# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .. import BaseApi, BaseModel

from ..exceptions import CannabisReportsValidationException

from ..models.effects_flavors import EffectsFlavors
from ..models.menu_item import MenuItemSummary
from ..models.review import Review
from ..models.user import User


class AbstractItemEndpoint(BaseApi):
    """This represents an abstract item endpoint.

    The Strains, Flowers, Extracts, Edibles, and Products APIs inherit from
    this.
    """

    @classmethod
    def get_user(cls, session, ucpc):
        """Get the user who added the object to the database.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want the user from.

        Returns:
            cannabis_reports.models.User: The user who added the object
                to the database.
        """
        return cls(
            '/%s/%s/user' % (cls.__endpoint__, ucpc),
            session=session,
            singleton=True,
            out_type=User,
        )

    @classmethod
    def get_reviews(cls, session, ucpc, limit=None):
        """Get the reviews for a cannabis object.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want the reviews from.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=cannabis_reports.models.Review):
                Reviews iterator.
        """
        return cls(
            '/%s/%s/reviews' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Review,
            iteration_limit=limit,
        )

    @classmethod
    def get_effects_flavors(cls, session, ucpc):
        """Get the average effects and flavors from reviews for this object.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want the effect and flavor profile
                from.

        Returns:
            cannabis_reports.models.EffectsFlavors: The effect and flavor
                profile for this object.
        """
        return cls(
            '/%s/%s/effectsFlavors' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=EffectsFlavors,
            singleton=True,
        )

    @classmethod
    def get_available(cls, session, ucpc, lat, lng, radius=10, limit=None):
        """Get information about the availability of the given UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis object you want the children from.
            lat (float): Latitude for the center of your availability search.
            lng (float): Longitude for the center of your availability search.
            radius (int): Radius to search for in miles, max 25.
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
                cls.__endpoint__, ucpc, lat, lng, radius,
            ),
            session=session,
            out_type=MenuItemSummary,
            iteration_limit=limit,
        )

    @classmethod
    def search(cls, session, query, sort=None, path='search', limit=None):
        """Return search results for objects.

        Args:
            session (requests.sessions.Session): Authenticated session.
            query (str): Search query to find objects in our system.
                Must be at least 2 characters.
            sort (str): Snake cased field name to sort on. Prefix with a `-`
                for descending.
            path (str): The path for the search (eg for ``strains`` it is
                ``search`` and for ``flowers`` it is ``type``.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=cls.__object__):
                Objects iterator.
        """
        if not query or len(query) < 2:
            raise CannabisReportsValidationException(
                'Search query must be at least 2 characters.',
            )
        data = {}
        if sort is not None:
            data['sort'] = BaseModel._to_camel_case(sort)
        return cls(
            '/%s/%s/%s' % (cls.__endpoint__, path, query),
            session=session,
            data=data,
            iteration_limit=limit,
        )
