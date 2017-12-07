# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item_endpoint import AbstractItemEndpoint

from ..models.extract import Extract
from ..models.producer import Producer


class Extracts(AbstractItemEndpoint):
    """This represents the ``Extracts`` Endpoint.

    https://developers.cannabisreports.com/docs/extracts
    """

    __object__ = Extract
    __endpoint__ = 'extracts'

    @classmethod
    def search(cls, session, extract_type, sort=None, path='type'):
        """Gets products for a given type with optional sorting.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis extract you want the genetics from.
            sort (str): Snake cased field name to sort on. Prefix with a `-`
                for descending.
            path (str): The path for the search (eg for ``strains`` it is
                ``search`` and for ``extracts`` it is ``type``.

        Returns:
            RequestPaginator(output_type=cannabis_reports.models.Extract):
                An iterator of parent extracts.
        """
        return super(Extracts, session, extract_type, sort, path)

    @classmethod
    def get_producer(cls, session, ucpc):
        """Gets the producer for a given extract.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis extract you want the seed company from.

        Returns:
            cannabis_reports.models.SeedCompany: The producer that was
                responsible for this extract.
        """
        return cls(
            '/extracts/%s/producer' % ucpc,
            session=session,
            out_type=Producer,
            singleton=True,
        )

    @classmethod
    def get_strain(cls, session, ucpc):
        """Gets the information about a strain for a extract with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis extract you want the genetics from.

        Returns:
            cannabis_reports.models.Strain: The strain for the extract.
        """
        return cls(
            '/extracts/%s/strain' % ucpc,
            session=session,
        )
