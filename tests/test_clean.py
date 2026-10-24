
import pandas as pd

from src.clean import limpar_dados


def test_remover_registros_invalidos():
    df = pd.DataFrame({
        "InvoiceNo": ["1001", "1002", "1003", "1004"],
        "StockCode": ["A", "B", "C", "D"],
        "Description": ["Produto A", "Produto B", "Produto C", "Produto D"],
        "Quantity": [2, -1, 3, 1],
        "InvoiceDate": ["2011-01-01"] * 4,
        "UnitPrice": [10.0, 20.0, 0.0, 5.0],
        "CustomerID": [101, 102, 103, 104],
        "Country": ["Brazil"] * 4,
    })

    resultado = limpar_dados(df)

    assert len(resultado) == 2
    assert (resultado["Quantity"] > 0).all()
    assert (resultado["UnitPrice"] > 0).all()


def test_calcular_faturamento():
    df = pd.DataFrame({
        "InvoiceNo": ["1001", "1002"],
        "StockCode": ["A", "B"],
        "Description": ["Produto A", "Produto B"],
        "Quantity": [2, 3],
        "InvoiceDate": ["2011-01-01"] * 2,
        "UnitPrice": [10.0, 5.0],
        "CustomerID": [101, 102],
        "Country": ["Brazil", "Brazil"],
    })

    resultado = limpar_dados(df)

    assert resultado["Revenue"].sum() == 35.0
