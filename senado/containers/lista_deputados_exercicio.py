# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from senado.core.containers.response import (
    SuccessContainerResponse
)


class GetAllParlamentaresRS(SuccessContainerResponse):
    """
    """
    def __init__(
        self,
        version='',
        version_service='',
        error=False,
        msg='',
        data=[]
    ):

        if not isinstance(data, list):
            raise ValueError(
                'Os itens precisam estar em uma lista'
            )

        self._data = data
        self._has_error = error
        self._msg = msg
        self._version = version
        self._version_service = version_service
