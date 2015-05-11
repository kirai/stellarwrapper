import requests
import json

URL = 'https://test.stellar.org:9002'
ACCOUNT_ADDRESS = ''

# Retrieves the balance from a account_info json response data
def get_account_balance(pum):
	balance = json.loads(pum.text)
	return balance['result']['account_data']['Balance']

# Getting account information
payload = { 'method' : 'account_info',
		    'params': [{'account': ACCOUNT_ADDRESS }]
		  }

print 'SENDING to ' + URL + ' ...'
print payload

pum = requests.post(URL, data= json.dumps(payload))
print 'RECEIVED from ' + URL
print pum.text

# Getting account balance
print '--------------------------------'
print 'Your current account balance is:'
print '--------------------------------'
print get_account_balance(pum) + ' Future Lab coins'
print '--------------------------------'




