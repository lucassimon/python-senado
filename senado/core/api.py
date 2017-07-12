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
