# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import six

from senado.core.containers.person import Pessoa


class Exercicio(object):
    """
    Classe que refere-se ao exercicio do mandato do Parlamentar
    """

    _codigo = None
    _data_inicio = None
    _data_fim = None
    _data_leitura = None
    _descricao_afastamento = None
    _sigla_afastamento = None

    def __init__(self, codigo, data_inicio):

        self._codigo = codigo

        self._data_inicio = data_inicio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):

        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):

        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):

        self._data_fim = value

    @property
    def data_leitura(self):
        return self._data_leitura

    @data_leitura.setter
    def data_leitura(self, value):

        self._data_leitura = value

    @property
    def descricao_afastamento(self):
        return self._descricao_afastamento

    @descricao_afastamento.setter
    def descricao_afastamento(self, value):

        self._descricao_afastamento = value

    @property
    def sigla_afastamento(self):
        return self._sigla_afastamento

    @sigla_afastamento.setter
    def sigla_afastamento(self, value):

        self._sigla_afastamento = value


class Suplente(Pessoa):
    """
    Suplente do parlamentar
    """
    pass


class Titular(Pessoa):
    """
    Titular do parlamentar
    """
    pass


class Legislatura(object):
    """
    Dados base da legislatura do mandato
    """

    _numero = None
    _data_inicio = None
    _data_fim = None

    def __init__(
        self,
        numero,
        data_inicio,
        data_fim,
    ):

        if not isinstance(data_inicio, datetime.date):

            raise ValueError("O campo data inicio é do tipo date")

        if not isinstance(data_fim, datetime.date):

            raise ValueError("O campo data fim é do tipo date")

        self._numero = numero
        self._data_inicio = data_inicio
        self.data_fim = data_fim


class Mandato(object):
    """
    Dados base do mandato
    """
    _codigo = None
    _uf = None
    _descricao = None
    _primeira_legislatura = None
    _segunda_legislatura = None
    _exercicios = []
    _suplentes = []
    _titular = None

    def __init__(
        self,
        codigo,
        uf,
        descricao,
        primeira_legislatura,
        segunda_legislatura
    ):

        self._codigo = codigo

        self._uf = uf

        self._descricao = descricao

        self._primeira_legislatura = primeira_legislatura

        self._segunda_legislatura = segunda_legislatura

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):

        self._codigo = value

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):

        self._uf = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):

        self._descricao = value

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):

        self._titular = value

    @property
    def suplentes(self):
        return self._suplentes

    @suplentes.setter
    def suplentes(self, value):

        self._suplentes = value

    @property
    def exercicios(self):
        return self._exercicios

    @exercicios.setter
    def exercicios(self, value):

        self._exercicios = value

    @property
    def primeira_legislatura(self):
        return self._primeira_legislatura

    @primeira_legislatura.setter
    def primeira_legislatura(self, value):

        self._primeira_legislatura = value

    @property
    def segunda_legislatura(self):
        return self._segunda_legislatura

    @segunda_legislatura.setter
    def segunda_legislatura(self, value):

        self._segunda_legislatura = value


class Parlamentar(object):
    """
    Atributos do parlamentar
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
    _mandato = None

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

    def __str__(self):

        return u'{} - {}'.format(
            self.nome,
            self.sigla_partido
        )

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
    def nome_completo(self):
        return self._nome_completo

    @nome_completo.setter
    def nome_completo(self, value):

        self._nome_completo = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):

        self._sexo = value

    @property
    def forma_tratamento(self):
        return self._forma_tratamento

    @forma_tratamento.setter
    def forma_tratamento(self, value):

        self._forma_tratamento = value

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, value):

        self._foto = value

    @property
    def pagina(self):
        return self._pagina

    @pagina.setter
    def pagina(self, value):

        self._pagina = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        self._email = value

    @property
    def sigla_partido(self):
        return self._sigla_partido

    @sigla_partido.setter
    def sigla_partido(self, value):

        self._sigla_partido = value

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):

        self._uf = value

    @property
    def mandato(self):
        return self._mandato

    @mandato.setter
    def mandato(self, value):

        self._mandato = value
