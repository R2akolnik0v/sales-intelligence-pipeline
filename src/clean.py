
import pandas as pd


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa os dados de vendas:
    - Remove linhas duplicadas.
    - Remove registros sem código de produto ou quantidade.
    - Remove quantidades e preços inválidos.
    """

    df = df.copy()

    # Remover linhas duplicadas
    df = df.drop_duplicates()

    # Remover registros sem informações essenciais
    df = df.dropna(subset=["InvoiceNo", "StockCode", "Quantity", "UnitPrice"])

    # Converter colunas numéricas
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

    # Manter apenas quantidades e preços positivos
    df = df.dropna(subset=["Quantity", "UnitPrice"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Criar coluna de receita
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    return df
