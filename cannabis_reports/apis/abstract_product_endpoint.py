# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item_endpoint import AbstractItemEndpoint

from ..models.producer import Producer
from ..models.strain import Strain


class AbstractProductEndpoint(AbstractItemEndpoint):
    """This represents an abstract product endpoint.

    The Edibles, Extracts, Flowers, Products APIs inherit from this.
    """

    @classmethod
    def get_producer(cls, session, ucpc):
        """Gets the producer for a given product.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis product you want the seed company from.

        Returns:
            cannabis_reports.models.SeedCompany: The producer that was
                responsible for this product.
        """
        return cls(
            '/%s/%s/producer' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Producer,
            singleton=True,
        )

    @classmethod
    def get_strain(cls, session, ucpc):
        """Gets the information about a strain for a product with the given
        UCPC.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code>`_ for
                the cannabis product you want the strain from.

        Returns:
            cannabis_reports.models.Strain: The strain for the product.
        """
        return cls(
            '/%s/%s/strain' % (cls.__endpoint__, ucpc),
            session=session,
            out_type=Strain,
            singleton=True,
        )
