import re
import pandas as pd

tickers = list()
finais_desejados = ['3', '4', '5', '6', '11']

with open('COTAHIST_A2015.TXT', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        if '201501' in linha:
            ticker = linha[12:].split()[0].strip()
            # Extrai apenas os dígitos finais do ticker
            match = re.match(r'([A-Z]+)(\d+)$', ticker)
            if match:
                final = match.group(2)
                if final in finais_desejados:
                    if ticker not in tickers:
                        tickers.append(ticker)
                      
novo_df = pd.DataFrame(tickers)
novo_df.to_csv('banco.csv', mode='a', header=False, index=False)