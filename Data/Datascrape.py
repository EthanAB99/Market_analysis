"""File for scraping data
 Key:	UZUm8ezpPOTHnfneTdyJlasqlN6ptACd

 
 """

from polygon import RESTClient as Rest

api_key = 'UZUm8ezpPOTHnfneTdyJlasqlN6ptACd'
client = Rest(api_key)

# Fetch previous close data for AMD
previous_close = client.get_previous_close("AMD")
print(previous_close)


