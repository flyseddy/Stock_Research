"""
Author: Sedrick Thomas
Created: May 2020
Stock Research

"""
import requests

# List of sample stocks we will get the price of 
stock_names = ['FB', 'BRK.B', 'MCD', 'JNJ', 'AMZN', 'AAPL', 'V', 'JPM', 'DIS']
stock_info_list = []
for stock_name in stock_names:
    url = f'https://financialmodelingprep.com/api/v3/company/profile/{stock_name}'
    # Make an API Call
    r = requests.get(url)
    print(f"Stock: {stock_name} - Status Code: {r.status_code}")
    stock_dict = r.json()

    # Build a dictionary for each stock
    try: 
        stock_info_dict = {
            'company': stock_dict['symbol'],
            'price': stock_dict['profile']['price'],
            'website': stock_dict['profile']['website'],
        }
    except KeyError:
        print(f"Cant access {stock_name}'s details")
    else:
        stock_info_list.append(stock_info_dict)

for stock_info in stock_info_list:
    print(f"\nCompany: {stock_info['company']}")
    print(f"Price: {stock_info['price']}")
    print(f"Website: {stock_info['website']}")

