# 🤑 Trading Bot 💶

It's a trading bot that I'm building using the [Alpaca API](https://github.com/alpacahq/alpaca-trade-api-python).

# Usage

Though in early stages, I'm currently building the bot according to an ETF called TQQQ that tracks the QQQ. TQQQ is a leveraged ETF, meaning that you have more buying power than your capital would allow you to.

At the end of this project I'd like to employ the bot for Mini FTSE MIB contracts, so it'll be operating on the Italian futures market.

# Features

The bot can do the following things:

* Submit *market* orders
* Retrieve up to 300 days of data for each ticker (open, close, high, low, vwap)
* Calculate RSI and MA values for each ticker
* Adjust positions based off of these values

# Additional things

Please, do not use this bot to trade your money if *you DO NOT understand* its content and the strategies utilized by it.
