"""
File for scraping data using Polygon.io
Key: UZUm8ezpPOTHnfneTdyJlasqlN6ptACd
"""

from polygon import RESTClient as Rest

api_key = 'UZUm8ezpPOTHnfneTdyJlasqlN6ptACd'
client = Rest(api_key)

response = client.get_previous_close_agg("AMD")

print("Previous Close Data for AMD:")
print(response)
