# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

import pytest

from requests.exceptions import (
    Timeout,
    HTTPError,
    ConnectionError,
    ProxyError,
    SSLError,
    ConnectTimeout,
    ReadTimeout,
    TooManyRedirects,
    RetryError
)


from senado.core.api import APIBase
from senado.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)
from senado.parse import SenadoParse
from senado.containers.lista_deputados_exercicio import (
    GetAllParlamentaresRS
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula
    """

    ENDPOINT = 'http://legis.senado.leg.br/dadosabertos/senador/lista/atual'

    def __init__(self):

        pass

    def lista_deputados_em_exercicio(self):
        """
        Retorna todos os parlamentares em exercicio
        """

        response = None

        try:

            response = requests.get(
                self.ENDPOINT,
                headers={
                    'Accept': 'application/json'
                }
            ).json()

        except ValueError as e:
            return ErrorRS(
                error=True,
                msg=e.message,
            )
        except (
            Timeout, HTTPError, ConnectionError,
            ProxyError, SSLError, ConnectTimeout,
            ReadTimeout, TooManyRedirects, RetryError
        ) as e:
            return ConnectionExceptionRS(
                error=True,
                msg=e.message,
                exception=e
            )
        except Exception as e:
            return ExceptionRS(
                error=True,
                msg=e.message,
            )

        if self._verifica_response_none(response):
            return ErrorRS(
                error=True,
                msg='Resposta nula ou vazia.'
            )

        # tratar os dados

        data = SenadoParse.parse(response)

        pytest.set_trace()

        data_rs = GetAllParlamentaresRS(
            error=False,
            version=response.get(
                'ListaParlamentarEmExercicio'
            ).get(
                'Metadados'
            ).get(
                'Versao'
            ),
            msg=response.get(
                'ListaParlamentarEmExercicio'
            ).get(
                'Metadados'
            ).get(
                'DescricaoDataSet'
            ),
            version_service=response.get(
                'ListaParlamentarEmExercicio'
            ).get(
                'Metadados'
            ).get(
                'VersaoServico'
            ),
            data=data
        )

        return data_rs
