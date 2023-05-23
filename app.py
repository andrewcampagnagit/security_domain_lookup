import requests
import os

h = {"User-ID":"andrew.campagna", "API-Key":"1rzZTSRNOsJoRm09QHt05fOXyiddJkxIPcoGxCoNSDw6VwFP"}
response = requests.post("https://neutrinoapi.net/domain-lookup", headers=h, json={"domain":os.environ["APP_INPUTS"]})

print(response.json())
