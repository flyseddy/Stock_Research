"""
Author: Sedrick Thomas
Created: May 2020
Writes to a CSV file the Company and Rating utilizing an API

"""


import requests
from csv import writer


stock_companies = ['FB', 'AAPL', 'TSLA', 'SNAP']
stock_info_list = []
for stock_name in stock_companies:
    url = f'https://financialmodelingprep.com/api/v3/company/rating/{stock_name}'
    r = requests.get(url)
    # Parses the request as a json
    stock_info = r.json()
    

    stock_info_dict = {
        'company': stock_info['symbol'],
        'rating': stock_info['rating']['score'],
    }
    stock_info_list.append(stock_info_dict)




with open('company_ratings.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Company', 'Rating']
    csv_writer.writerow(headers)
    for stock in stock_info_list:
        company = stock['company']
        rating = stock['rating']
        csv_writer.writerow([company, rating])

    






