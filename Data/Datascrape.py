"""
File for scraping data using Polygon.io
"""

from polygon import RESTClient as Rest


client = Rest(api_key)

response = client.get_previous_close_agg("AMD")

print("Previous Close Data for AMD:")
print(response)
