import pandas as pd
from pathlib import Path

pasta = Path("dados/cotahist")

# CODBDI: 02 = lote padrão, 05 = regime especial/sanções, 08 = recuperação judicial
CODBDI_ACOES = {"02", "05", "08"}

registros = []
for caminho in sorted(pasta.glob("*.TXT")):
    with open(caminho, 'r', encoding='latin-1') as arquivo:
        next(arquivo)  # header
        for linha in arquivo:
            if linha[:2] != "01":
                continue
            codbdi = linha[10:12]
            ticker = linha[12:24].strip()
            if codbdi not in CODBDI_ACOES:
                continue
            if linha[24:27] != "010":  # TPMERC: apenas mercado à vista (exclui opções, termo, fracionário)
                continue
            if linha[39:42] == "IBO":  # ESPECI: exclui índice (IBOV11)
                continue
            if not (len(ticker) == 5 or ticker[4:6] == "11"):
                continue
            fatcot = int(linha[210:217])  # FATCOT: preços são cotados por lote de FATCOT ações
            registros.append((
                linha[2:10],
                ticker,
                codbdi,
                linha[27:39].strip(),
                int(linha[56:69]) / 100 / fatcot,   # PREABE
                int(linha[69:82]) / 100 / fatcot,   # PREMAX
                int(linha[82:95]) / 100 / fatcot,   # PREMIN
                int(linha[108:121]) / 100 / fatcot, # PREULT
                int(linha[152:170]),                # QUATOT: quantidade negociada
                int(linha[170:188]) / 100,          # VOLTOT: volume financeiro
            ))

df = pd.DataFrame(registros, columns=["data", "ticker", "codbdi", "nome", "abertura",
                                      "maxima", "minima", "fechamento", "quantidade", "volume"])
df["data"] = pd.to_datetime(df["data"], format="%Y%m%d")
df.to_parquet('cotacoes.parquet', engine='pyarrow', compression='snappy')
