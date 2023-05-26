import requests
import os

h = {"User-ID":"andrew.campagna", "API-Key":"1rzZTSRNOsJoRm09QHt05fOXyiddJkxIPcoGxCoNSDw6VwFP"}
response = requests.get("https://www.neutrinoapi.net/domain-lookup", headers=h, data={"host":os.environ["APP_INPUTS"],"live":"true"})

print(response.json())
