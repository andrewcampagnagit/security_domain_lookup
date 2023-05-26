import requests
import os

h = {"User-ID":"andrew.campagna", "API-Key":"1rzZTSRNOsJoRm09QHt05fOXyiddJkxIPcoGxCoNSDw6VwFP"}
response = requests.get("34.96.127.102/domain-lookup", headers=h, data={"host":os.environ["APP_INPUTS"],"live":"true"})

print(response.json())
