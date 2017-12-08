# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .. import BaseApi

from ..models.dispensary import Dispensary
from ..models.edible import Edible
from ..models.extract import Extract
from ..models.product import Product
from ..models.strain import Strain


class Dispensaries(BaseApi):
    """This represents the ``Dispensaries`` Endpoint.

    https://developers.cannabisreports.com/docs/dispensaries
    """

    __object__ = Dispensary
    __endpoint__ = 'dispensaries'

    @classmethod
    def get(cls, session, slug):
        raise NotImplementedError

    @classmethod
    def get_by_slug(cls, session, state, city, slug):
        """Gets information about an individual dispensary based on the
        state, city, and slug

        Args:
            session (requests.sessions.Session): Authenticated session.
            city (str): City the dispensary is in.
            state (str): Two character state for the dispensary.
            slug (str): Slug for the name of the dispensary.

        Returns:
            Dispensary: The dispensary.
        """
        return cls(
            '/%s/%s/%s/%s' % (
                cls.__endpoint__, state, city, slug,
            ),
            session=session,
        )

    @classmethod
    def get_strains(cls, session, state, city, slug):
        """Gets a paginated list of strains for a dispensary with the
        given slug.

        Args:
            session (requests.sessions.Session): Authenticated session.
            city (str): City the dispensary is in.
            state (str): Two character state for the dispensary.
            slug (str): Slug for the name of the dispensary.

        Returns:
            RequestPaginator(output_type=Strain):
                The strains for this dispensary.
        """
        return cls(
            '/%s/%s/%s/%s/strains' % (
                cls.__endpoint__, state, city, slug,
            ),
            session=session,
            out_type=Strain,
        )

    @classmethod
    def get_extracts(cls, session, state, city, slug):
        """Gets a paginated list of extracts for a dispensary with the
        given slug.

        Args:
            session (requests.sessions.Session): Authenticated session.
            city (str): City the dispensary is in.
            state (str): Two character state for the dispensary.
            slug (str): Slug for the name of the dispensary.

        Returns:
            RequestPaginator(output_type=Extract):
                The extracts for this dispensary.
        """
        return cls(
            '/%s/%s/%s/%s/extracts' % (
                cls.__endpoint__, state, city, slug,
            ),
            session=session,
            out_type=Extract,
        )

    @classmethod
    def get_edibles(cls, session, state, city, slug):
        """Gets a paginated list of edibles for a dispensary with the given
        slug.

        Args:
            session (requests.sessions.Session): Authenticated session.
            city (str): City the dispensary is in.
            state (str): Two character state for the dispensary.
            slug (str): Slug for the name of the dispensary.

        Returns:
            RequestPaginator(output_type=Edible):
                The edibles for this dispensary.
        """
        return cls(
            '/%s/%s/%s/%s/edibles' % (
                cls.__endpoint__, state, city, slug,
            ),
            session=session,
            out_type=Edible,
        )

    @classmethod
    def get_products(cls, session, state, city, slug):
        """Gets a paginated list of products for a dispensary with the given
        slug.

        Args:
            session (requests.sessions.Session): Authenticated session.
            city (str): City the dispensary is in.
            state (str): Two character state for the dispensary.
            slug (str): Slug for the name of the dispensary.

        Returns:
            RequestPaginator(output_type=Product):
                The products for this dispensary.
        """
        return cls(
            '/%s/%s/%s/%s/products' % (
                cls.__endpoint__, state, city, slug,
            ),
            session=session,
            out_type=Product,
        )
