import pandas as pd
import os

endereco_pasta = r"C:\Users\Danillo\Documents\Teste_automacao"
arquivo_1 = "[Teste] Teste automacao - Conciliacao_Mensal.csv"
arquivo_2 = "[Teste] Teste automacao relatorio - Conciliacao_Mensal.csv"

def import_csv(nome_arquivo, endereco_pasta):
    try:
        arquivo = os.path.join(endereco_pasta, nome_arquivo)
        resultado = pd.read_csv(arquivo)
        #print(resultado)
        return resultado
    except Exception as e:
        print(f"Erro na tentativa da leitura do {arquivo}: {e}")

def pegar_colunas(resultado,colunas):
    if resultado is not None:
        return resultado[colunas]

print(pegar_colunas(import_csv(arquivo_1,endereco_pasta), ["contrato", "qa", "valor_iq", "valor_pp", "diferenca"]))
#pegar_colunas(import_csv(arquivo_2,endereco_pasta), ["contract", "amount","account_type","bill_item","description"])

def analisar_contratos()

# def analisar_contratos(df, colunas_a_verificar):
#     if df is not None:
#         for index, row in df.iterrows():
#             contrato = row['contrato']
#             colunas_nao_zero = [coluna for coluna in colunas_a_verificar if row[coluna] != 0]
#             if colunas_nao_zero:
#                 print(f"Contrato {contrato}:")
#                 for coluna in colunas_nao_zero:
#                     print(f"  Coluna {coluna} tem valor {row[coluna]}")

# # Importar e pegar as colunas do primeiro arquivo
# resultado = import_csv(arquivo_1, endereco_pasta)
# colunas_desejadas = ["contrato", "qa", "valor_iq", "valor_pp", "diferenca"]
# novo_df = pegar_colunas(resultado, colunas_desejadas)

# # Analisar os contratos
# colunas_a_verificar = ["qa", "valor_iq", "valor_pp"]