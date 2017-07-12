# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class ContainerResponse(object):

    _has_error = False
    _msg = ''

    def __init__(self, error=False, msg=''):

        self._has_error = error
        self._msg = msg

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):

        self._has_error = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value


class SuccessContainerResponse(ContainerResponse):

    """
    Container de sucesso
    """

    _data = []

    def __init__(self, error=False, msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os itens precisam estar em uma lista'
            )

        self._data = data
        self._has_error = error
        self._msg = msg

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'Os itens precisam estar em uma lista'
            )

        self._data = value
