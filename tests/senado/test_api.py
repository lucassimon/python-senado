# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import pytest
import unittest
import datetime
from dateutil.relativedelta import relativedelta

from senado.api import API
from senado.containers.lista_deputados_exercicio import GetAllParlamentaresRS


class SenadoTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.api = API()


class SenadoTestCase(SenadoTestCaseBase):
    """
    Testes para o serviço do senado
    """

    def test_sucesso_lista_deputados_em_exercicio(self):

        res = self.api.lista_deputados_em_exercicio()

        self.assertIsInstance(res, GetAllParlamentaresRS)
