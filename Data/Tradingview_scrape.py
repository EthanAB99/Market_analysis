"""
File for taking and sorting important data from tradingview and other sources to get a wholistic view of markets
"""

from tradingview_ta import TA_Handler, Interval, Exchange

aapl_handler = TA_Handler(
    symbol="AAPL",
    exchange="NASDAQ",
    screener="america",
    interval=Interval.INTERVAL_1_DAY
)

analysis = aapl_handler.get_analysis()

print("RSI:", analysis.indicators["RSI"])
print("MACD:", analysis.indicators["MACD.macd"])
print("MACD Signal:", analysis.indicators["MACD.signal"])
print("Volume:", analysis.indicators["volume"])
print("BB Upper:", analysis.indicators.get("BB.upper", "N/A"))
print("BB Lower:", analysis.indicators.get("BB.lower", "N/A"))
