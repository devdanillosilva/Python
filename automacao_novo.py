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

def analisar_contratos(output_concilicao, output_query):
    if output_conciliacao and output_query is not None:
        contrato = output_conciliacao.get("contrato")
        quintoandar_amount = output_conciliacao.get("qa")
        iq_amount = output_conciliacao.get("valor_iq")
        pp_amount = output_conciliacao.get("valor_pp")
        diferenca = output_conciliacao.get("diferenca")
        total_iq_amount = 0
        total_pp_amount = 0
        for index, row in output_query.iterrows():
            amount = row.get("amount")
            account_type = row.get("account_type")
            if amount = quintoandar_amount:
                print(f"quintoandar_amount é igual a amount,{amount}")
            elif amount = iq_amount:
                print(f"iq_amount é igual a amount,{amount}")
            elif amount = pp_amount:
                print(f"pp_amount é igual a amount,{amount}")
            if account_type = "tenant":
                total_iq_amount += amount
            if account_type = "landlord":
                total_pp_amount += amount
        print(total_pp_amount,total_iq_amount)

def main()
    output_conciliacao = pegar_colunas(import_csv(arquivo_1,endereco_pasta), ["contrato", "qa", "valor_iq", "valor_pp", "diferenca"])
    output_query = pegar_colunas(import_csv(arquivo_2,endereco_pasta), ["contract", "amount","account_type","bill_item","description"])
    for index, row in output_conciliacao.iterrows():
        print(f"Lendo a linha {index}, com o conteúdo {row}")
        analisar_contratos(row, output_query)

if__name__=="__main__":
    main()

# # Importar e pegar as colunas do primeiro arquivo
# resultado = import_csv(arquivo_1, endereco_pasta)
# colunas_desejadas = ["contrato", "qa", "valor_iq", "valor_pp", "diferenca"]
# novo_df = pegar_colunas(resultado, colunas_desejadas)

# # Analisar os contratos
# colunas_a_verificar = ["qa", "valor_iq", "valor_pp"]
