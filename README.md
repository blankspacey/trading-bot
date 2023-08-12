# 🤑 Trading Bot 💶

It's a trading bot that I'm building using the [Alpaca API](https://github.com/alpacahq/alpaca-trade-api-python).

# Usage

Though in early stages, I'm currently building the bot according to an ETF called TQQQ that tracks the QQQ. TQQQ is a leveraged ETF, meaning that basically if the market is down 5 basis points, you're down 10/15/20/50 basis points depending on how leveraged the asset you're trading is. In this case TQQQ is leveraged 3 times QQQ, so if QQQ is down 5%, you're down 15%.

Leveraged assets are seriously risky. **DO NOT trade assets such as options, futures, CFDs** if you don't know what you're getting into as you may incur in big losses if proper risk and portfolio management is not implemented correctly in the strategy.

At the end of this project I'd like to employ the bot for Mini FTSE MIB contracts, so it'll be operating on the Italian futures market.

# Features

The bot can do the following things:

* Submit **market** orders
* Retrieve up to 300 days of data for each ticker (open, close, high, low, vwap)
* Calculate RSI and MA values for each ticker
* Adjust positions based off of these values
* Send emails to alert you of any order submission or attempt to submit an order

# Additional things

Please, do not use this bot to trade your money if **you DO NOT understand** its content and the strategies utilized by it.
