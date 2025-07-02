"""
Plan: Scraping Desired Features from TradingView (and Other Sources Where Needed)

This script will collect the following: 
- From Yahoo finance
  -Take simple OHCLV data
  -derive indicators (RSI, MACD, etc)
  - 

- From Other Sources:
  - Global Liquidity: from FRED or BIS data (e.g. M2 Money Supply)
  - VIX: Yahoo Finance ('^VIX') or CBOE API
  - 10Y/30Y Yield: FRED (DGS10, DGS30)
  - P/E Ratio: Yahoo Finance / Finviz scraping
  - Fed Funds Rate: FRED ('FEDFUNDS')

- Derived Tags (calculated):
  - Liquidity expanding vs contracting: rolling average of M2 vs current M2
  - Volatility tag: classify VIX values
  - Whale accumulation/distribution: to be derived from order book data (later)

Dependencies:
- Use `tvDatafeed` or `tradingview_ta` for indicator data (depending on what works)
- `pandas` for feature engineering
- `yfinance` for FRED proxies, VIX, P/E where needed
- `requests/bs4` for custom scraping

To Do:
1. Set up ticker list (e.g. AAPL, TSLA, BTCUSD, SPX, NDX)
2. Test `tradingview_ta` for RSI, MACD, BBands
3. Fall back to `tvDatafeed` if more detailed chart data needed
4. Combine with external API for macro/fundamentals (e.g. FRED for yield curve)
5. Create tags/labels from rolling indicators (e.g. M2 growth, VIX thresholds)
6. Add order book scraping from Binance (crypto) or bookmap-style from Level 2 providers

Start with TradingView indicators in the next cell.
"""
