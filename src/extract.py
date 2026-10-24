
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

def carregar_dados() -> pd.DataFrame:
    """Carrega o arquivo Excel original de vendas."""

    arquivos = list(RAW_DIR.glob("*.xlsx"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo .xlsx encontrado em {RAW_DIR}. "
            "Coloque o arquivo original de vendas nessa pasta."
        )

    arquivo = arquivos[0]
    print(f"Carregando arquivo: {arquivo.name}")

    df = pd.read_excel(arquivo)

    print(f"Linhas carregadas: {len(df)}")
    print(f"Colunas encontradas: {list(df.columns)}")

    return df


if __name__ == "__main__":
    carregar_dados()


