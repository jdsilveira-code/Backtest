import pandas as pd

tickers = list()    

with open('dados/cotahist/COTAHIST_A2015.TXT', 'r', encoding='latin-1') as arquivo:
    for linha in arquivo:
        if linha[:2] != "01":
            continue
        if len(linha[12:23].strip()) == 5:
            tickers.append(linha[12:23].strip())     
df = pd.DataFrame(tickers, columns=['ticker'])
df.to_parquet('dados.parquet', engine='pyarrow', compression='snappy')
