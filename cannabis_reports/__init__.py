# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from requests import Session

from .auth_proxy import AuthProxy
from .base_api import BaseApi
from .base_model import BaseModel

from . import exceptions


class CannabisReports(object):
    """This object is the primary point of interaction with CannabisReports.

    Properties will be set on this ``CannabisReports`` instance that will
    mirror the class names of APIs in the ``cannabis_reports.api`` module.

    These API classes are naive of authentication, so the actual properties
    set will be using the ``AuthProxy`` class, which will transparently
    inject authentication into the API requests while still allowing for a
    naive API object.

    This allows for the ``CannabisReports`` instance to act as a container for
    all of the authenticated API objects.

    Examples::

        from cannabis_reports import CannabisReports
        cr = CannabisReports('api_key')
        for strain in cr.Strains.list():
            print(strain.serialize())
    """

    __apis__ = {}

    def __init__(self, api_key=None):
        """Initialize a new CannabisReports client.

        Args:
            api_key (str, optional): The API key to use for this session.
        """
        self.session = Session()
        if api_key:
            self.session.headers.update({
                'X-API-Key': api_key,
            })
        self._load_apis()

    def _load_apis(self):
        """Find available APIs and set instances property auth proxies."""
        cannabis_reports = __import__('cannabis_reports.apis')
        for class_name in cannabis_reports.apis.__all__:
            if not class_name.startswith('_'):
                cls = getattr(cannabis_reports.apis, class_name)
                api = AuthProxy(self.session, cls)
                setattr(self, class_name, api)
                self.__apis__[class_name] = api


__all__ = [
    'AuthProxy',
    'BaseApi',
    'BaseModel',
    'exceptions',
    'CannabisReports',
]
