import pandas as pd
from pathlib import Path

dados_tickers = dict()
pasta = Path("dados/cotahist")

for caminho in sorted(pasta.glob("*.TXT")):
    tickers = set()
    with open(caminho, 'r', encoding='latin-1') as arquivo:
        ano = next(arquivo)[11:15]
        for linha in arquivo:
            if linha[:2] != "01":
                continue
            if linha[10:12] != "02":
                continue
            if len(linha[12:24].strip()) == 5 or linha[16:18] == "11":
                tickers.add(linha[12:24].strip())
    dados_tickers[ano] = sorted(tickers)

registros = [(ano, t) for ano, lista in dados_tickers.items() for t in lista]
df = pd.DataFrame(registros, columns=["ano", "ticker"])
df.to_parquet('tickers.parquet', engine='pyarrow', compression='snappy')
