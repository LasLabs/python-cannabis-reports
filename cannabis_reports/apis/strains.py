# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item_endpoint import AbstractItemEndpoint

from ..models.seed_company import SeedCompany
from ..models.strain import Strain


class Strains(AbstractItemEndpoint):
    """This represents the ``Strains`` Endpoint.

    https://developers.cannabisreports.com/docs/strains
    """

    __object__ = Strain
    __endpoint__ = 'strains'

    @classmethod
    def get_seed_company(cls, session, ucpc):
        """Get the seed company that was responsible for a cannabis strain.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis strain you want the seed company from.

        Returns:
            cannabis_reports.models.SeedCompany: The seed company that was
                responsible for this strain.
        """
        return cls(
            '/strains/%s/seedCompany' % ucpc,
            session=session,
            out_type=SeedCompany,
            singleton=True,
        )

    @classmethod
    def get_genetics(cls, session, ucpc):
        """Gets the strains that were the parent material for the strain
        with the given UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis strain you want the genetics from.

        Returns:
            RequestPaginator(output_type=cannabis_reports.models.Strain):
                An iterator of parent strains.
        """
        return cls(
            '/strains/%s/genetics' % ucpc,
            session=session,
        )

    @classmethod
    def get_children(cls, session, ucpc, limit=None):
        """Get the child strains that this one has been bred into.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis strain you want the children from.
            limit (int, optional): Stop after iterating this many pages.

        Returns:
            RequestPaginator(output_type=cannabis_reports.models.Strain):
                An iterator of child strains.
        """
        return cls(
            '/strains/%s/children' % ucpc,
            session=session,
            iteration_limit=limit,
        )
