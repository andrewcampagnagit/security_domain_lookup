import requests
import os

h = {"User-ID":"andrew.campagna", "API-Key":"1rzZTSRNOsJoRm09QHt05fOXyiddJkxIPcoGxCoNSDw6VwFP"}
p = [("host",os.environ["APP_INPUTS"]),("live","true")]
response = requests.get("https://neutrinoapi.net/domain-lookup", headers=h, params=p)
data = response.json()
print(data)
