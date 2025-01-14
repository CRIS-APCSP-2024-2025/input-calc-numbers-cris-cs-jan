'''
Jan, Grade 12, APCSP
Assignment: Celcius to Fahrenheit

This program will prompt the user to input Celcius temperature 
and output the equivalent Fahrenheit temperature.
'''

# prompt the user for input and store the value as a string variable 
cel_str = input('Enter a Celcius temperature as a float: ')

# convert string to float 
cel = float(cel_str)

# convert celcius to fahrenheit using this formula:
fahrenheit = (cel * 1.8) + 32

# print results
print('Temperature in Fahrenheit: ', fahrenheit)