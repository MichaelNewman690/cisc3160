'''This lab was written in python which i litterally learnt today nd uses the openweather API.
originally i used a API wrapper class called pyown but i wasnt sure whether you wanted us to access the api directly so
i switched to directly. This fulfills problems 2 and 3'''

import requests
#asks the user for a city
city = input('Enter City: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=dded5321576939a877e5e9919c0407db'.format(city)

res = requests.get(url)

data =res.json()

#temp in kelvin
current_temp = data['main']['temp']
print('Current Temperature in', city, 'is', current_temp, 'in Kelvin')

#conversion to celsius
current_temp = current_temp-273.15

print('Current Temperature in', city, 'is', current_temp, 'in Celsius')

#conversion to fahrehnheit
current_temp = current_temp*9/5 + 32

print('Current Temperature in', city, 'is', current_temp, 'in Fahrenheit')