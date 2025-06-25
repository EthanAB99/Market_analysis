"""
File for scraping data using Polygon.io
"""

from polygon import RESTClient as Rest
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path = ".env.local")
API_KEY = os.getenv("POLYGON_API_KEY")
if not API_KEY:
    raise ValueError("put the api key in the .env.local file")

client = Rest(API_KEY)

response = client.get_previous_close_agg("PLTR")
RSI = client.get_rsi('PLTR')
MACD = client.get_macd('PLTR')


print("Previous Close Data for PLTR:")
print(response)
print('RSI data:')
print(RSI)
print('MACD data:')
print(MACD)

