# Como rodar o ambiente da API

## Algumas informações

A api e feita em `python` usando `fastapi` e esta rodando em um ambiente virtual python com suas dependências ja instaladas.


O repositório principal do Gastos DF pode ser visualizado clicando <a href="https://github.com/unb-mds/Gastos-DF-Squad12">aqui</a>.

A documentação do projeto pode ser visualizada clicando <a href="https://unb-mds.github.io/2024-1-Gastos-DF-Doc-Squad12/">aqui</a>.

## Pré-requisitos

Ter o Python 3.12.3 ou superior instalado.

Ter o pip 24.0 ou superior instalado.

### No Windows

Tentei. Não roda, ativa o WSL ou instala um ubuntu e segue os passos do linux 👍

### No linux (ubuntu)

Dentro da pasta `api` execulte os seguintes comandos:

Para ativar o ambiente virtual do python execute:
```
source venv/bin/activate
```

Em seguida para abrir um servidor local e visualizar no seu navegador execute:
```
python3 main.py
```

Será aberto no endereço http://localhost:8001/

O seu docs estará no endereço http://localhost:8001/docs

Mais informações sobre o ambiente virtal python podem ser encontrado em https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

