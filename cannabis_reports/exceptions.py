# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class CannabisReportsException(Exception):
    """Base exception for CannabisReports library errors."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class CannabisReportsRemoteException(CannabisReportsException):
    """Indicates that an error occurred when communicating with the remote."""

    def __init__(self, status_code, message):
        self.status_code = status_code
        super(CannabisReportsRemoteException, self).__init__(message)

    def __str__(self):
        return '(%d) %s' % (self.status_code, self.message)


class CannabisReportsValidationException(CannabisReportsException):
    """Indicates an error while validating user-supplied data."""


class CannabisReportsSecurityException(CannabisReportsException):
    """Indicates a security error; probably by an invalid web hook signature.
    """
