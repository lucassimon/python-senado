# python-senado

Biblioteca em python para buscar através de API os dados dos senadores brasileiros.

## Como utilizar

Instalar o pacote python-senado

Importe os dados de `from senado.api import API as SenadoAPI`

Métodos disponíveis:

* lista_deputados_em_exercicio

## Testes

Para executar o teste é necessário ter instalado os pacotes de desenvolvimento em seu virtualenv.

`pip install requirements-dev`

Em seguida execute `pytest`

Para visualizar os resultados pode-se colocar um breakpoint `pytest.set_trace()` no arquivo `tests/senado/test_api.py` linha 30 e percorrer a instancia do objeto `res` conforme a sua especificação da classe
`GetAllParlamentaresRS` e de seus dados atributo `data` da  `class Parlamentar`


## Arquitetura do pacote

Estrutura e comentarios acerca de cada modulo

```
.
├── api.py #  Pasta contendo a classe de comunicacao e seus métodos
├── containers # Pasta contendo os containers dos metodos
│   ├── __init__.py
│   ├── lista_deputados_exercicio.py # Possui o container de responsta deste metodo
│   ├── parlamentar.py # Possui as classes OO referente aos dados dos senadores
│   └── response.py #
├── core
│   ├── api.py # Classe base para API
│   ├── containers # Pasta contendo classes abstratas
│   │   ├── error.py # Classes para informar um Erro de conexao ou de resposta
│   │   ├── __init__.py
│   │   ├── person.py # Classe abstrata para pessoa (titular/suplementar)
│   │   └── response.py # Classes para resposta dos dados
│   └── __init__.py
├── __init__.py
├── parse.py # Classes para manipulação dos dados

```



