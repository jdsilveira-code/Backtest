import pandas as pd

tickers = list()    

with open('dados/cotahist/COTAHIST_A2015.TXT', 'r', encoding='latin-1') as arquivo:
    for linha in arquivo:
        if linha[:2] != "01":
            continue
        if linha[16:17] == 11:
            print(linha[16:17])

