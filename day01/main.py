# Band Name Generation

print('What is the name of city you were born in?')
city_name = input()

if city_name == '':
    print('You must enter the city name. Otherwise, we can not proceed.')

print('What is your pet name?')
pet_name = input()

if pet_name == '':
    print('You must enter your pet name. Otherwise, we can not proceed.')

print('Your band name should be ' + city_name + pet_name + '.')

