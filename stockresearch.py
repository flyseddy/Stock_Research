import requests


# Make an API call and store the response
url = 'https://financialmodelingprep.com/api/v3/company/profile/AAPL'

r = requests.get(url)
print(f"Status code: {r.status_code}")

# Store the reponse in a variable
stock_dict = r.json()


# Process the results
price = stock_dict['profile']['price']
print(price)
