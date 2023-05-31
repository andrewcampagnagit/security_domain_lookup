import requests
import os

h = {"User-ID":"andrew.campagna", "API-Key":"1rzZTSRNOsJoRm09QHt05fOXyiddJkxIPcoGxCoNSDw6VwFP"}

def get_domain_info(dns_name):

	p = [("host",dns_name),("live","true")]
	response = requests.get("https://neutrinoapi.net/domain-lookup", 
							headers=h, 
							params=p)
	data = response.json()
	message = "This domain contains \n"
	for item in data["sensors"]:
		message += "- "+ item["description"] +"\n"
	print(message)

def get_ip_addr_info(ipv4_addr):

	p = [("ip",ipv4_addr)]
	response = requests.get("https://neutrinoapi.net/ip-blocklist", 
							headers=h, 
							params=p)
	data = response.json()
	message = "This domain contains \n"
	for item in data["sensors"]:
		message += "- "+ item["description"] +"\n"
	print(message)

inputs = os.environ["APP_INPUTS"].split(",")

if inputs[0] == "DNS Name":
	get_domain_info(inputs[1])

if inputs[0] == "IP Address":
	get_ip_addr_info(inputs[1])
