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


from lms.core.api import APIBase
from lms.core.containers.login import LoginRQ
from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    """
    ENDPOINT = 'http://legis.senado.leg.br/dadosabertos/senador/lista/atual'

    def __init__(self, passport):

        pass

    def lista_deputados_em_exercicio(self, paginate_rq):
        """
        Retorna todos os parlamentares em exercicio
        """

        response = None

        try:

            response = requests.get(self.ENDPOINT)

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

        data = SenadoParse.get_all(response)

        data_rs = GetAllStudentRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

