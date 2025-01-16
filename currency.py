'''
Jan, Grade 12, APCSP
Assignment: Currency Conversion

This program will prompt the user to input a number of US Dollars (USD)
and output the equivalent amount of Thai Baht.
'''

# prompt the user to input and store the value as a string variable
USD_str = input('Enter currency amount in USD: ')

# convert string to float 
USD = float(USD_str)

# convert currency in USD to Thai baht using this exchange rate:
exchange_rate = 33.6887 * USD
THB = (exchange_rate)

# print results
print(THB, "Thai Baht")
