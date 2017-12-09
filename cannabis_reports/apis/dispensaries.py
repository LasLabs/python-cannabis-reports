# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_entity_endpoint import AbstractEntityEndpoint

from ..models.dispensary import Dispensary
from ..models.strain import Strain


class Dispensaries(AbstractEntityEndpoint):
    """This represents the ``Dispensaries`` Endpoint.

    https://developers.cannabisreports.com/docs/dispensaries
    """

    __object__ = Dispensary
    __endpoint__ = 'dispensaries'

    @classmethod
    def get_strains(cls, session, slug, limit=None):
        """Gets a paginated list of strains for a dispensary with the
        given slug.

        Args:
            session (requests.sessions.Session): Authenticated session.
            slug (str): Slug for the name of the dispensary (includes
                city/state slug).
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=Strain):
                The strains for this dispensary.
        """
        return cls(
            '/%s/%s/strains' % (cls.__endpoint__, slug),
            session=session,
            out_type=Strain,
            iteration_limit=limit,
        )

    @classmethod
    def get_available(cls, *args, **kwargs):
        raise NotImplementedError(
            'This endpoint does not implement availability searches.',
        )
