# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class APIBase(object):
    """
    Api para servico
    """

    def _verifica_response_none(self, res):

        if res is None:

            return True

        return False

    def _verifica_response_has_error(self, res):

        if res['hasError']:

            return True

        return False

    def _verifica_exception(self, res, execption_class=Exception):

        if res['hasError']:
            raise execption_class(res['Msg'])
