"""
File for scraping data using Polygon.io
Key: UZUm8ezpPOTHnfneTdyJlasqlN6ptACd
"""

from polygon import RESTClient
import os

API_KEY = "UZUm8ezpPOTHnfneTdyJlasqlN6ptACd"
client = RESTClient(API_KEY)

response = client.get_previous_close("AMD")

print("Previous Close Data for AMD:")
print(response)
