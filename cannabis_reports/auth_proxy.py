# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class AuthProxy(object):
    """This object acts as a transparent authentication proxy for the API.

    This is required because the API objects are naive of the authentication
    that is setup in ``CannabisReports``, and all of the API interface
    methods are ``classmethods`` because they are instantiating.
    """

    # These methods will not pass through to ``proxy_class``.
    METHOD_NO_PROXY = [
        'auth_proxy',
    ]

    def __init__(self, session, proxy_class):
        """Instantiate an API Authentication Proxy.

        Args:
            auth (requests.Session): Authenticated requests Session.
            proxy_class (type): A class implementing the ``BaseApi``
             interface.
        """
        assert isinstance(proxy_class, type)
        self.session = session
        self.proxy_class = proxy_class

    def __getattr__(self, item):
        """Override attribute getter to act as a proxy for``proxy_class``.

        If ``item`` is contained in ``METHOD_NO_PROXY``, it will not be
        proxied to the ``proxy_class`` and will instead return the attribute
        on this object.

        Args:
            item (str): Name of attribute to get.
        """
        if item in self.METHOD_NO_PROXY:
            return super(AuthProxy, self).__getattr__(item)
        attr = getattr(self.proxy_class, item)
        if callable(attr):
            return self.auth_proxy(attr)

    def auth_proxy(self, method):
        """Authentication proxy for API requests.

        This is required because the API objects are naive of
        ``CannabisReports``, so they would otherwise be unauthenticated.

        Args:
            method (callable): A method call that should be authenticated. It
             should accept a ``requests.Session`` as its first parameter,
             which should be used for the actual API call.

        Returns:
            mixed: The results of the authenticated callable.
        """
        def _proxy(*args, **kwargs):
            """The actual proxy, which instantiates and authenticates the API.

            Args:
                *args (mixed): Args to send to class instantiation.
                **kwargs (mixed): Kwargs to send to class instantiation.

            Returns:
                mixed: The result of the authenticated callable.
            """
            return method(self.session, *args, **kwargs)

        return _proxy
