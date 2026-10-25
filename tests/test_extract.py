
import pandas as pd
import pytest

import src.extract as extract


def test_carregar_dados(monkeypatch, tmp_path, capsys):
    arquivo = tmp_path / "vendas.xlsx"

    # Cria um Excel pequeno para o teste
    df_original = pd.DataFrame({
        "InvoiceNo": ["1001", "1002"],
        "Quantity": [2, 3],
        "UnitPrice": [10.0, 5.0],
    })
    df_original.to_excel(arquivo, index=False)

    monkeypatch.setattr(extract, "RAW_DIR", tmp_path)

    resultado = extract.carregar_dados()

    assert len(resultado) == 2
    assert list(resultado.columns) == [
        "InvoiceNo", "Quantity", "UnitPrice"
    ]

    saida = capsys.readouterr().out
    assert "vendas.xlsx" in saida
    assert "Linhas carregadas: 2" in saida


def test_erro_quando_nao_existe_excel(monkeypatch, tmp_path):
    monkeypatch.setattr(extract, "RAW_DIR", tmp_path)

    with pytest.raises(FileNotFoundError, match="Nenhum arquivo"):
        extract.carregar_dados()

