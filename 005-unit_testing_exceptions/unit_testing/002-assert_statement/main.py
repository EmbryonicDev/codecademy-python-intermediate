destinations = {
    'BUD': 'Budapest',
    'CMN': 'Casablanca',
    'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below:

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)
