# Sales Intelligence Pipeline

Projeto de análise de dados de vendas desenvolvido com Python, Pandas, SQL e SQLite, com o objetivo de transformar dados brutos em indicadores de negócio e visualizações úteis para a tomada de decisão.

## Objetivo

Construir um pipeline de dados capaz de extrair, limpar, analisar e armazenar dados de vendas, gerando indicadores de desempenho e relatórios que podem apoiar análises comerciais.

## Tecnologias utilizadas

- **Python** — desenvolvimento do pipeline.
- **Pandas** — limpeza, transformação e análise de dados.
- **SQLite** — armazenamento e consultas SQL.
- **Matplotlib** — criação de gráficos.
- **Git e GitHub** — versionamento e publicação do projeto.

## Fonte dos dados

Dataset **Online Retail**, disponibilizado pelo UCI Machine Learning Repository.

Fonte: https://archive.ics.uci.edu/dataset/352/online%2Bretail

O conjunto de dados contém registros de transações de uma empresa varejista entre 2010 e 2011.

## Etapas do projeto

1. **Extração:** leitura dos dados originais em Excel.
2. **Limpeza:** remoção de duplicidades, registros incompletos e valores inválidos.
3. **Transformação:** cálculo do faturamento por item a partir de quantidade e preço unitário.
4. **Armazenamento:** exportação dos dados tratados para CSV e banco SQLite.
5. **Análise:** cálculo de indicadores e identificação dos produtos e países com maior desempenho.
6. **Visualização:** geração de gráfico de faturamento mensal.
7. **Relatórios:** exportação dos indicadores gerais para CSV.

## Principais resultados

Após o processo de limpeza, foram obtidos os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Registros originais | 541.909 |
| Registros após limpeza | 524.878 |
| Faturamento calculado | £10.642.110,80 |
| Unidades vendidas | 5.572.420 |
| Transações distintas | 19.960 |
| Países distintos | 38 |
| Produtos distintos | 3.922 |

**Observação:** o faturamento representa os registros mantidos após a limpeza. Como quantidades negativas foram excluídas, devoluções não são contabilizadas nesse indicador.

## Estrutura do projeto

```text
sales-intelligence-pipeline/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sales.db
├── outputs/
│   ├── charts/
│   └── reports/
├── src/
│   ├── extract.py
│   ├── clean.py
│   ├── analysis.py
│   └── database.py
├── main.py
├── requirements.txt
└── README.md
```

## Arquivos gerados

- `data/processed/online_retail_limpo.csv` — dados tratados.
- `data/sales.db` — banco de dados SQLite.
- `outputs/charts/faturamento_mensal.png` — gráfico de faturamento por mês.
- `outputs/reports/indicadores_vendas.csv` — relatório de indicadores gerais.

## Como executar

1. Clone ou baixe o repositório.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Coloque o arquivo original `Online Retail.xlsx` em `data/raw/`.
4. Execute o pipeline:

```bash
python main.py
```

Para gerar o gráfico e o relatório a partir do banco SQLite já criado:

```bash
python src/analysis.py
```

## Aprendizados

Este projeto permitiu praticar extração e tratamento de dados, criação de métricas de negócio, consultas SQL, persistência em banco de dados e geração de relatórios automatizados.

## Autor

Projeto desenvolvido para fins de aprendizado e construção de portfólio na área de Análise de Dados.