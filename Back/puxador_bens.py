import requests
import re

# Fazendo a solicitação GET para a API
response = requests.get(
    'https://queridodiario.ok.org.br/api/gazettes?territory_ids=5300108&published_since=2024-01-01&published_until=2024-07-01&querystring=%22EXTRATO%20DO%20CONTRATO%20DE%20AQUISI%C3%87%C3%83O%20DE%20BENS%22&excerpt_size=4000&number_of_excerpts=10000&pre_tags=&post_tags=&size=10000&sort_by=descending_date')

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:

    # Convertendo a resposta para JSON
    dados = response.json()

    # Acessando a lista de gazettes dentro dos dados
    gazettes = dados['gazettes']

    # Conjunto para armazenar as datas já vistas
    datas_vistas = set()

    # Iterando sobre cada gazette na lista
    for gazette in gazettes:
        # Acessando a data de cada gazette
        data = gazette['date']

        # Verificando se a data já foi impressa
        if data not in datas_vistas:
            print("\nData:", data)
            # Adicionando a data ao conjunto de datas vistas
            datas_vistas.add(data)

        # Acessando a lista de excertos de cada gazette
        excertos = gazette['excerpts']
        total_diario = 0

        # Iterando sobre cada excerto
        for excerto in excertos:
            # Remover quebras de linha no meio das palavras
            excerto = re.sub(r'(\w)-\n(\w)', r'\1\2', excerto)
            # Remover todas as quebras de linha
            excerto = excerto.replace('\n', ' ')

            # Usando expressão regular para encontrar Empresa, CNPJ, Objeto e Valor
            empresa_match = re.search(r'(?:FORNECEDOR|empresa)\s+([\w\s\-ÇçÉéÁáÍíÓóÚúÃãÕõâêîôûÂÊÎÔÛäëïöüÄËÏÖÜ]+)\s+.*?CNPJ[\s:nº]*([\d./-]+)', excerto, re.DOTALL)
            objeto_match = re.search(r'OBJETO:\s*([^\n,]+?(?:,\s*para atender as demandas)?(?:\s*da Vice-Governadoria)?.*?)\s*VALOR', excerto, re.DOTALL)
            valor_match = re.search(r'VALOR (?:DO CONTRATO)?:\s*R\$ ([\d,.]+)', excerto)

            if empresa_match and objeto_match and valor_match:
                # Extraindo a empresa e o CNPJ encontrados
                empresa = empresa_match.group(1).strip()
                cnpj = empresa_match.group(2).strip()

                # Extraindo o objeto encontrado e removendo parte desnecessária
                objeto = objeto_match.group(1).strip()

                # Extraindo o valor encontrado
                valor = valor_match.group(1)
                # Removendo caracteres não numéricos, exceto vírgulas e pontos
                valor_limpo = re.sub(r'[^\d,.]', '', valor)
                # Removendo pontos extras como separadores de milhar
                valor_limpo = valor_limpo.replace('.', '')
                # Trocando a vírgula por ponto para ter o formato correto para float
                valor_limpo = valor_limpo.replace(',', '.')
                # Convertendo o valor para float
                valor_float = float(valor_limpo)
                total_diario += valor_float

                print(f"Empresa: {empresa} -- CNPJ: {cnpj}\nObjeto: {objeto}\nValor: R${valor_float:.2f}")
        print(f'Dívidas totais = R${total_diario:.2f}')
else:
    # Se a solicitação falhar, imprima o código de status
    print("Erro:", response.status_code)