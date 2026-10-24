
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_DIR / "data" / "sales.db"
CHARTS_DIR = PROJECT_DIR / "outputs" / "charts"
REPORTS_DIR = PROJECT_DIR / "outputs" / "reports"


def analisar_vendas(df: pd.DataFrame) -> dict:
    """Gera indicadores gerais de vendas a partir de um DataFrame limpo."""

    if df.empty:
        raise ValueError("Não existem dados para analisar.")

    faturamento_total = df["Revenue"].sum()
    quantidade_vendida = df["Quantity"].sum()
    total_transacoes = df["InvoiceNo"].nunique()

    produtos_mais_vendidos = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    faturamento_por_pais = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "faturamento_total": faturamento_total,
        "quantidade_vendida": quantidade_vendida,
        "total_transacoes": total_transacoes,
        "produtos_mais_vendidos": produtos_mais_vendidos,
        "faturamento_por_pais": faturamento_por_pais,
    }


def gerar_grafico_faturamento_mensal():
    """Gera e salva o gráfico de faturamento por mês."""

    with sqlite3.connect(DB_PATH) as conexao:
        consulta = """
            SELECT
                substr(InvoiceDate, 1, 7) AS mes,
                ROUND(SUM(Revenue), 2) AS faturamento
            FROM vendas
            GROUP BY mes
            ORDER BY mes;
        """
        df = pd.read_sql_query(consulta, conexao)

    if df.empty:
        print("Não existem dados para gerar o gráfico.")
        return

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df["mes"], df["faturamento"], marker="o")
    plt.title("Faturamento Mensal")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (£)")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    caminho = CHARTS_DIR / "faturamento_mensal.png"
    plt.savefig(caminho, dpi=300)
    plt.close()

    print(f"Gráfico salvo em: {caminho}")


def gerar_relatorio_indicadores():
    """Consulta o banco e salva os indicadores gerais em CSV."""

    with sqlite3.connect(DB_PATH) as conexao:
        consulta = """
            SELECT
                ROUND(SUM(Revenue), 2) AS faturamento_total,
                SUM(Quantity) AS quantidade_vendida,
                COUNT(DISTINCT InvoiceNo) AS total_transacoes,
                COUNT(DISTINCT Country) AS total_paises,
                COUNT(DISTINCT StockCode) AS total_produtos
            FROM vendas;
        """

        df = pd.read_sql_query(consulta, conexao)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    caminho = REPORTS_DIR / "indicadores_vendas.csv"
    df.to_csv(caminho, index=False, encoding="utf-8-sig")

    print("\n--- Relatório de Indicadores ---")
    print(df.to_string(index=False))
    print(f"\nRelatório salvo em: {caminho}")


if __name__ == "__main__":
    gerar_grafico_faturamento_mensal()
    gerar_relatorio_indicadores()
