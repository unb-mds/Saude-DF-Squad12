# Como rodar o ambiente da documentação

## Algumas informações

O deploy é feito automaticamente e pode ser acompanhado na aba `actions` do git hub. O arquivo
`index.md` é a página inicial da documentação para criar uma página nova apenas crie um arquivo `.md`
na pasta `docs` a documentação toda é feita em `markdown` para mais detalhes visite a documentação.

## Clonando esta branch

```
git clone -b documentacao <link do repositório>
```

## Pré-requisitos

Ter o Python 3.12.3 ou superior instalado.

Ter o pip 24.0 ou superior instalado.

### No Windows

Tentei. Não roda, ativa o WSL ou instala um ubuntu e segue os passos do linux 👍

### No linux (ubuntu)

Para ativar o ambiente virtual do python execute:
```
source venv/bin/activate
```

Em seguida para abrir um servidor local e visualizar no seu navegador execute:
```
mkdocs serve
```

Será aberto no endereço http://localhost:8000/

Caso tenha problemas para subir o servidor local execute:
```
pip3 install --upgrade mkdocs mkdocs-material
```

Mais informações sobre o ambiente virtal python podem ser encontrado em https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

