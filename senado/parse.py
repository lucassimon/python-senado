# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import pytest

from senado.containers.parlamentar import (
    Parlamentar, Mandato, Legislatura, Exercicio, Titular, Suplente
)


class SenadoParse(object):
    """
    Parse dos dados vindo do response
    """

    @staticmethod
    def get_parlamentar(parlamentar):
        """
        Cria uma instancia da classe Parlamentar
        """

        errors = []

        try:
            codigo = parlamentar.get(
                'CodigoParlamentar'
            )
        except Exception as e:

            # Logar exception

            # Gerar uma lista de erros
            errors.append(e)

            codigo = ''

        try:
            nome = parlamentar.get(
                'NomeParlamentar'
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            nome = ''

        try:
            nome_completo = parlamentar.get(
                'NomeCompletoParlamentar'
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            nome_completo = ''

        try:
            sexo = parlamentar.get(
                'SexoParlamentar'
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            sexo = ''

        try:
            forma_tratamento = parlamentar.get(
                'FormaTratamento'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            forma_tratamento = ''

        try:
            foto = parlamentar.get(
                'UrlFotoParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            foto = ''

        try:
            pagina = parlamentar.get(
                'UrlPaginaParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            pagina = ''

        try:
            email = parlamentar.get(
                'EmailParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            email = ''

        try:
            sigla_partido = parlamentar.get(
                'SiglaPartidoParlamentar'
            ).strip()

        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            sigla_partido = ''

        try:
            uf = parlamentar.get(
                'UfParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            uf = ''

        return Parlamentar(
            codigo=codigo,
            nome=nome,
            nome_completo=nome_completo,
            sexo=sexo,
            forma_tratamento=forma_tratamento,
            foto=foto,
            pagina=pagina,
            email=email,
            sigla_partido=sigla_partido,
            uf=uf
        )

    @staticmethod
    def get_mandato(mandato):
        """
        Cria uma instancia da classe Mandato
        """

        errors = []

        try:
            codigo = mandato.get(
                'CodigoMandato'
            )
        except Exception as e:

            # Logar exception

            # Gerar uma lista de erros
            errors.append(e)

            codigo = ''

        try:
            descricao = mandato.get(
                'DescricaoParticipacao'
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            descricao = ''

        try:
            uf = mandato.get(
                'UfParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            uf = ''

        try:
            numero = mandato.get(
                'PrimeiraLegislaturaDoMandato'
            ).get(
                'NumeroLegislatura'
            )

            data_inicio = mandato.get(
                'PrimeiraLegislaturaDoMandato'
            ).get(
                'DataInicio'
            )

            data_inicio = datetime.strptime(
                data_inicio,
                '%Y-%m-%d'
            )

            data_fim = mandato.get(
                'PrimeiraLegislaturaDoMandato'
            ).get(
                'DataFim'
            )

            data_fim = datetime.strptime(
                data_fim,
                '%Y-%m-%d'
            )

            primeira_legislatura = Legislatura(
                numero=numero,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            primeira_legislatura = ''

        try:
            numero = mandato.get(
                'SegundaLegislaturaDoMandato'
            ).get(
                'NumeroLegislatura'
            )

            data_inicio = mandato.get(
                'SegundaLegislaturaDoMandato'
            ).get(
                'DataInicio'
            )

            data_inicio = datetime.strptime(
                data_inicio,
                '%Y-%m-%d'
            )

            data_fim = mandato.get(
                'SegundaLegislaturaDoMandato'
            ).get(
                'DataFim'
            )

            data_fim = datetime.strptime(
                data_fim,
                '%Y-%m-%d'
            )

            segunda_legislatura = Legislatura(
                numero=numero,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            segunda_legislatura = ''

        return Mandato(
            codigo=codigo,
            uf=uf,
            descricao=descricao,
            primeira_legislatura=primeira_legislatura,
            segunda_legislatura=segunda_legislatura
        )

    @staticmethod
    def get_exercicios(ws_exercicios):
        """
        Cria uma instância da classe Suplente
        """

        exercicios = []

        if isinstance(exercicios, list):

            for sup in ws_exercicios:

                try:
                    codigo = sup.get('CodigoExercicio')
                except Exception:
                    codigo = ''

                try:
                    data_inicio = sup.get(
                        'DataInicio'
                    )

                    data_inicio = datetime.strptime(
                        data_inicio,
                        '%Y-%m-%d'
                    )
                except Exception:
                    data_inicio = ''

                exercicio = Exercicio(
                    codigo=codigo,
                    data_inicio=data_inicio
                )

                if 'DataFim' in sup:

                    try:
                        data_fim = sup.get(
                            'DataFim'
                        )

                        data_fim = datetime.strptime(
                            data_fim,
                            '%Y-%m-%d'
                        )
                    except Exception:
                        data_fim = ''

                    exercicio.data_fim = data_fim

                if 'DataLeitura' in sup:

                    try:
                        data_leitura = sup.get(
                            'DataLeitura'
                        )

                        data_leitura = datetime.strptime(
                            data_leitura,
                            '%Y-%m-%d'
                        )
                    except Exception:
                        data_leitura = ''

                    exercicio.data_leitura = data_leitura

                if 'DescricaoCausaAfastamento' in sup:

                    try:
                        descricao_afastamento = sup.get(
                            'DescricaoCausaAfastamento'
                        )

                    except Exception:
                        descricao_afastamento = ''

                    exercicio.descricao_afastamento = descricao_afastamento

                if 'SiglaCausaAfastamento' in sup:

                    try:
                        sigla_afastamento = sup.get(
                            'SiglaCausaAfastamento'
                        )
                    except Exception:
                        sigla_afastamento = ''

                    exercicio.sigla_afastamento = sigla_afastamento

                exercicios.append(
                    exercicio
                )

        return exercicios

    @staticmethod
    def get_suplentes(ws_suplentes):
        """
        Cria uma instancia da classe Suplente
        """

        suplentes = []

        if isinstance(ws_suplentes, list):

            for sup in ws_suplentes:

                suplentes.append(
                    SenadoParse.get_pessoa(sup)
                )

        else:

            suplentes.append(
                SenadoParse.get_pessoa(ws_suplentes)
            )

        return suplentes

    @staticmethod
    def get_pessoa(pessoa):
        """
        Cria uma instancia da classe que pode ser um Titular / Suplente
        """

        errors = []

        try:
            codigo = pessoa.get(
                'CodigoParlamentar'
            )
        except Exception as e:

            # Logar exception

            # Gerar uma lista de erros
            errors.append(e)

            codigo = ''

        try:
            descricao = pessoa.get(
                'DescricaoParticipacao'
            )
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            descricao = ''

        try:
            nome = pessoa.get(
                'NomeParlamentar'
            ).strip()
        except Exception as e:
            # Gerar uma lista de erros
            errors.append(e)

            nome = ''

        if descricao == 'Titular':

            return Titular(
                codigo=codigo,
                nome=nome,
                descricao=descricao
            )

        elif 'Suplente' in descricao:

            return Suplente(
                codigo=codigo,
                nome=nome,
                descricao=descricao
            )

        else:

            return errors

    @staticmethod
    def parse(response):
        """
        Parse de todos os dados
        """

        data = []

        try:
            parlamentares = response.get(
                'ListaParlamentarEmExercicio'
            ).get(
                'Parlamentares'
            ).get(
                'Parlamentar'
            )
        except Exception:
            return data

        for p in parlamentares:

            parlamentar = SenadoParse.get_parlamentar(
                p.get('IdentificacaoParlamentar')
            )

            mandato = SenadoParse.get_mandato(
                p.get('Mandato')
            )

            if 'Titular' in p.get('Mandato'):

                titular = SenadoParse.get_pessoa(
                    p.get('Mandato').get('Titular')
                )

                mandato.titular = titular

            suplentes = SenadoParse.get_suplentes(
                p.get('Mandato').get('Suplentes').get('Suplente')
            )

            mandato.suplentes = suplentes

            exercicios = SenadoParse.get_exercicios(
                p.get('Mandato').get('Exercicios').get('Exercicio')
            )

            mandato.exercicios = exercicios

            parlamentar.mandato = mandato

            data.append(parlamentar)

        return data
