# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six

from senado.core.containers.response import (
    ContainerResponse
)


class ErrorRS(ContainerResponse):

    pass


class ExceptionRS(ErrorRS):

    _exception = None

    def __init__(self, error=False, msg='', exception=None):

        self._has_error = error
        self._msg = msg

        if exception:
            self._exception = exception

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, value):

        self._exception = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value


class ConnectionExceptionRS(ExceptionRS):

    pass
