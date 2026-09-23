import yfinance as yf

Ticker = yf.Ticker("PETR4.SA")
info = Ticker.info
dre_anual = Ticker.income_stmt
indicadores = {
    "preco":     info.get("currentPrice"),
    "p/l":       info.get("trailingPE"),
    "EV/EBITDA": info.get("enterpriseToEbitda")  
}

ebit_historico = dre_anual.loc['Operating Income']
print(ebit_historico)