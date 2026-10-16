# Backtest
Estrutura de algoritmo para back test da b3

## Dados

O algoritmo utiliza arquivos de dados que não são versionados (os `.csv` estão no `.gitignore`), entre eles:

- **COTAHIST** (B3): séries históricas de cotações, em `dados/cotahist/`
- **DFP** (CVM): demonstrações financeiras padronizadas, em `dados/dfp/`
- **ITR** (CVM): informações trimestrais, em `dados/itr/`
- **FCA** (CVM): formulário cadastral, em `dados/fca/`

O layout do arquivo COTAHIST está em `docs/SeriesHistoricas_Layout.pdf`.


1º passo: Limpar COTAHIST mas mantendo duplicidade, data, nome_empresa, preco_fechamento, volume, quantidade_negociada
2º passo: vincular os tickers ao nome da empresa e cnpj
3º passo: Extrair indicadores por data e ativo