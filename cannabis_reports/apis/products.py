# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .abstract_item_endpoint import AbstractItemEndpoint

from ..models.product import Product
from ..models.producer import Producer


class Products(AbstractItemEndpoint):
    """This represents the ``Products`` Endpoint.

    https://developers.cannabisreports.com/docs/products
    """

    __object__ = Product
    __endpoint__ = 'products'

    @classmethod
    def search(cls, session, product_type, sort=None, path='type'):
        """Gets products for a given type with optional sorting.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis product you want the genetics from.
            sort (str): Snake cased field name to sort on. Prefix with a `-`
                for descending.
            path (str): The path for the search (eg for ``strains`` it is
                ``search`` and for ``products`` it is ``type``.

        Returns:
            RequestPaginator(output_type=cannabis_reports.models.Product):
                An iterator of parent products.
        """
        return super(Products, session, product_type, sort, path)

    @classmethod
    def get_producer(cls, session, ucpc):
        """Gets the producer for a given product.

        Args:
            session (requests.sessions.Session): Authenticated session.
            ucpc (str): `UCPC <https://developers.cannabisreports.com/
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis product you want the seed company from.

        Returns:
            cannabis_reports.models.SeedCompany: The producer that was
                responsible for this product.
        """
        return cls(
            '/products/%s/producer' % ucpc,
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
                v1.0/docs/ucpc-universal-cannabis-product-code`_ for
                the cannabis product you want the genetics from.

        Returns:
            cannabis_reports.models.Strain: The strain for the product.
        """
        return cls(
            '/products/%s/strain' % ucpc,
            session=session,
        )
