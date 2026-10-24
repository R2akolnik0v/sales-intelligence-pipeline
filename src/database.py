
import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_DIR / "data"
DB_PATH = DB_DIR / "sales.db"

def salvar_no_banco(df: pd.DataFrame, tabela: str = "vendas") -> None:
    """Salva os dados tratados em uma tabela SQLite."""

    DB_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conexao:
        df.to_sql(tabela, conexao, if_exists="replace", index=False)

    print(f"Dados salvos no banco: {DB_PATH}")




def consultar_vendas_por_pais():
    with sqlite3.connect(DB_PATH) as conexao:
        consulta = """
            SELECT
                Country,
                ROUND(SUM(Revenue), 2) AS faturamento
            FROM vendas
            GROUP BY Country
            ORDER BY faturamento DESC
            LIMIT 10;
        """

        resultado = pd.read_sql_query(consulta, conexao)
        print(resultado)


if __name__ == "__main__":
    consultar_vendas_por_pais()



def consultar_vendas_por_mes():
    with sqlite3.connect(DB_PATH) as conexao:
        consulta = """
            SELECT
                substr(InvoiceDate, 1, 7) AS mes,
                ROUND(SUM(Revenue), 2) AS faturamento
            FROM vendas
            GROUP BY mes
            ORDER BY mes;
        """

        resultado = pd.read_sql_query(consulta, conexao)
        print(resultado)
