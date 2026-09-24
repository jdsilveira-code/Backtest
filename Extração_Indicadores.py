import yfinance as yf

Ticker = yf.Ticker("PETR4.SA")
info = Ticker.info
dre_anual = Ticker.financials
balanco = Ticker.balance_sheet
ano_desejado = "2024"

indicadores = {
    "preco":      info.get("currentPrice"),
    "p/l":        info.get("trailingPE"),
    "EV/EBITDA":  info.get("enterpriseToEbitda"),  
}
coluna_ano = [col for col in balanco.columns if str(col.year) == ano_desejado]

ano_alvo = coluna_ano[0]
ativo_circulante = balanco.loc["Current Assets", ano_alvo]
try:
    imobilizado = balanco.loc["Net PPE", ano_alvo]
except KeyError:
    imobilizado = balanco.loc["Gross PPE", ano_alvo]
print(ativo_circulante, imobilizado)