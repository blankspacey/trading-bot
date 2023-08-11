from keys import *
import datetime as dt
import pandas as pd
import numpy as np
import talib as ta
import telegram as tg
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import TimeInForce, OrderSide
from alpaca.data.requests import StockBarsRequest, TimeFrame, DataFeed
from alpaca.data.historical import StockHistoricalDataClient