# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class Pessoa(object):
    """
    Classe pessoa para designar um parlamentar
    """
    _codigo = None
    _nome = None
    _descricao = None

    def __init__(self, codigo, nome, descricao):

        self._codigo = codigo

        self._nome = nome

        self._descricao = descricao

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):

        self._codigo = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):

        self._nome = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):

        self._descricao = value
