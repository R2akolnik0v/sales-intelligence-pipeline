
from pathlib import Path

from src.extract import carregar_dados
from src.clean import limpar_dados
from src.database import salvar_no_banco
from src.analysis import analisar_vendas

PROJECT_DIR = Path(__file__).resolve().parent
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
ARQUIVO_SAIDA = PROCESSED_DIR / "online_retail_limpo.csv"


def main():
    # Carregar os dados originais
    df = carregar_dados()

    # Limpar os dados
    df_limpo = limpar_dados(df)

    # Criar a pasta de saída
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Salvar o CSV tratado
    df_limpo.to_csv(ARQUIVO_SAIDA, index=False)

    # Salvar no banco SQLite
    salvar_no_banco(df_limpo)

    # Analisar as vendas
    resultados = analisar_vendas(df_limpo)

    print("\n--- Indicadores de vendas ---")
    print(f"Faturamento total: £{resultados['faturamento_total']:,.2f}")
    print(f"Quantidade vendida: {resultados['quantidade_vendida']:,}")
    print(f"Total de transações: {resultados['total_transacoes']:,}")

    print("\n--- Top 10 produtos por quantidade vendida ---")
    print(resultados["produtos_mais_vendidos"])

    print("\n--- Top 10 países por faturamento ---")
    print(resultados["faturamento_por_pais"])

    # Mostrar resumo
    print("\n--- Resumo do processamento ---")
    print(f"Linhas originais: {len(df)}")
    print(f"Linhas após limpeza: {len(df_limpo)}")
    print(f"CSV salvo em: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()

