from config import *

today = dt.date.today()
start_date = today - dt.timedelta(days=300)
end_date = today

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY, raw_data=True)

def get_prices(ticker, limit):
    stock_bars_data = StockBarsRequest(
    symbol_or_symbols=ticker, 
    start=pd.to_datetime(start_date),
    end=pd.to_datetime(end_date), 
    timeframe=TimeFrame.Day,
    limit=limit
    )

    barset = data_client.get_stock_bars(stock_bars_data)
    bars = pd.DataFrame(barset[ticker])

    return bars

def get_rsi(data, period):
    return ta.RSI(data['c'], timeperiod=period)

def get_moving_average(data, window):
    return data['c'].rolling(window=window).mean()

def open_position(ticker, amount):
    cash_available = float(trading_client.get_account().cash)

    market_order_data = MarketOrderRequest(
        symbol=ticker,
        notional=cash_available - (cash_available % 5),
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    )
    
    if cash_available >= amount:
        trading_client.submit_order(market_order_data)
        return True
    else:
        print("Not enough funds to execute trade.\n")
        return False

def close_position(ticker):
    market_order_data = MarketOrderRequest(
        symbol=ticker,
        qty='all',
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC
    )

    trading_client.submit_order(market_order_data)

def main():
    # tickers
    spy_ticker = 'SPY'
    tqqq_ticker = 'TQQQ'
    uvxy_ticker = 'UVXY'
    tecl_ticker = 'TECL'
    upro_ticker = 'UPRO'
    sqqq_ticker = 'SQQQ'
    tlt_ticker = 'TLT'

    # indicator periods
    spy_ma_period = 200
    tqqq_rsi_period = 10
    tlt_rsi_period = 10
    spxl_rsi_period = 10
    spy_rsi_period = 10
    tqqq_ma_period = 20
    sqqq_rsi_period = 10

    # prices
    spy_data = get_prices(spy_ticker, spy_ma_period)
    tqqq_data = get_prices(tqqq_ticker, max(tqqq_rsi_period, tqqq_ma_period))
    spxl_data = get_prices(spy_ticker, spxl_rsi_period)
    sqqq_data = get_prices(spy_ticker, tqqq_rsi_period)
    tlt_data = get_prices(tlt_ticker, tlt_rsi_period)

    # calculate indicators
    spy_rsi = get_rsi(spy_data, spy_rsi_period)[1]
    tqqq_rsi = get_rsi(tqqq_data, tqqq_rsi_period)[1]
    spxl_rsi = get_rsi(spxl_data, spxl_rsi_period)[1]
    tqqq_ma = get_moving_average(tqqq_data, tqqq_ma_period)[1]
    sqqq_rsi = get_rsi(sqqq_data, sqqq_rsi_period)[1]

    # current prices
    spy_current_price = float(spy_data['c'].iloc[-1])
    tqqq_current_price = float(tqqq_data['c'].iloc[-1])

    # strat execution
    if spy_current_price > get_moving_average(spy_data, spy_ma_period)[1]:
        if tqqq_rsi > 79:
            open_position(uvxy_ticker, float(trading_client.get_account().cash))
            if spxl_rsi > 80:
                open_position(uvxy_ticker, float(trading_client.get_account().cash))
            else:
                open_position(tqqq_ticker, float(trading_client.get_account().cash))
    else:
        if tqqq_rsi < 31:
            open_position(tecl_ticker, float(trading_client.get_account().cash))
        else:
            if spy_rsi < 30:
                open_position(upro_ticker, float(trading_client.get_account().cash))
            else:
                if tqqq_current_price < tqqq_ma:
                    if sqqq_rsi > get_rsi(tlt_data, 10)[-1]:
                        open_position(sqqq_ticker, float(trading_client.get_account().cash))
                    else:
                        open_position(tlt_ticker, float(trading_client.get_account().cash))
                else:
                    if sqqq_rsi < 31:
                        open_position(sqqq_ticker, float(trading_client.get_account().cash))
                    else:
                        open_position(tqqq_ticker, float(trading_client.get_account().cash))

if __name__ == "__main__":
    main()