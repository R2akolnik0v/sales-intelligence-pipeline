
import pandas as pd

from src.analysis import analisar_vendas


def test_calcular_indicadores_de_vendas():
    df = pd.DataFrame({
        "InvoiceNo": ["1001", "1001", "1002"],
        "StockCode": ["A", "B", "A"],
        "Description": ["Produto A", "Produto B", "Produto A"],
        "Quantity": [2, 3, 4],
        "UnitPrice": [10.0, 5.0, 10.0],
        "Revenue": [20.0, 15.0, 40.0],
        "Country": ["Brazil", "Brazil", "Portugal"],
    })

    resultado = analisar_vendas(df)

    assert resultado["faturamento_total"] == 75.0
    assert resultado["quantidade_vendida"] == 9
    assert resultado["total_transacoes"] == 2
    assert resultado["produtos_mais_vendidos"]["Produto A"] == 6


def test_erro_com_dataframe_vazio():
    df = pd.DataFrame()

    try:
        analisar_vendas(df)
    except ValueError as erro:
        assert str(erro) == "Não existem dados para analisar."
    else:
        assert False, "Era esperado um ValueError para dados vazios."
