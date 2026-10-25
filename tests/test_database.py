
import sqlite3

import pandas as pd

import src.database as database


def test_salvar_no_banco(monkeypatch, tmp_path):
    banco_teste = tmp_path / "teste.db"
    monkeypatch.setattr(database, "DB_PATH", banco_teste)

    df = pd.DataFrame({
        "InvoiceNo": ["1001", "1002"],
        "Country": ["Brazil", "Portugal"],
        "Revenue": [100.0, 50.0],
        "InvoiceDate": ["2011-01-01", "2011-02-01"],
    })

    database.salvar_no_banco(df)

    conexao = sqlite3.connect(banco_teste)
    try:
        resultado = pd.read_sql_query(
            "SELECT * FROM vendas", conexao
        )
    finally:
        conexao.close()

    assert len(resultado) == 2
    assert resultado["Revenue"].sum() == 150.0


def test_consultar_vendas_por_pais(monkeypatch, tmp_path, capsys):
    banco_teste = tmp_path / "teste.db"
    monkeypatch.setattr(database, "DB_PATH", banco_teste)

    conexao = sqlite3.connect(banco_teste)
    try:
        pd.DataFrame({
            "Country": ["Brazil", "Brazil", "Portugal"],
            "Revenue": [100.0, 50.0, 80.0],
        }).to_sql("vendas", conexao, index=False)
    finally:
        conexao.close()

    database.consultar_vendas_por_pais()

    saida = capsys.readouterr().out

    assert "Brazil" in saida
    assert "150.0" in saida
    assert "Portugal" in saida
    assert "80.0" in saida


def test_consultar_vendas_por_mes(monkeypatch, tmp_path, capsys):
    banco_teste = tmp_path / "teste.db"
    monkeypatch.setattr(database, "DB_PATH", banco_teste)

    conexao = sqlite3.connect(banco_teste)
    try:
        pd.DataFrame({
            "InvoiceDate": [
                "2011-01-05",
                "2011-01-20",
                "2011-02-10",
            ],
            "Revenue": [100.0, 50.0, 80.0],
        }).to_sql("vendas", conexao, index=False)
    finally:
        conexao.close()

    database.consultar_vendas_por_mes()

    saida = capsys.readouterr().out

    assert "2011-01" in saida
    assert "150.0" in saida
    assert "2011-02" in saida
    assert "80.0" in saida
