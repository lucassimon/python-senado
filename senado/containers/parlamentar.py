# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six


class Parlamentar(object):
    """

    """

    _codigo = None
    _nome = None
    _nome_completo = None
    _sexo = None
    _forma_tratamento = None
    _foto = None
    _pagina = None
    _email = None
    _sigla_partido = None
    _uf = None

    def __init__(
        self, codigo, nome, nome_completo, sexo, forma_tratamento,
        foto, pagina, email, sigla_partido, uf
    ):

        self._codigo = codigo

        self._nome = nome

        self._nome_completo = nome_completo

        self._sexo = sexo

        self._forma_tratamento = forma_tratamento

        self._foto = foto

        self._pagina = pagina

        self._email = email

        self._sigla_partido = sigla_partido

        self._uf = uf

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):

        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):

        self._nome = nome


    @property
    def nome_completo(self):
        return self._nome_completo

    @nome_completo.setter
    def nome_completo(self, value):

        self._nome_completo = nome_completo



    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):

        self._sexo = sexo


    @property
    def forma_tratamento(self):
        return self._forma_tratamento

    @forma_tratamento.setter
    def forma_tratamento(self, value):

        self._forma_tratamento = forma_tratamento


    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, value):

        self._foto = foto



    @property
    def pagina(self):
        return self._pagina

    @pagina.setter
    def pagina(self, value):

        self._pagina = pagina



    @property
    def email(self):
        return self._email

    @codigo.setter
    def email(self, value):

        self._email = email


    @property
    def sigla_partido(self):
        return self._sigla_partido

    @sigla_partido.setter
    def sigla_partido(self, value):

        self._sigla_partido = sigla_partido

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):

        self._uf = uf
