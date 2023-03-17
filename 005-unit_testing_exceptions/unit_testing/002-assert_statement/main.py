destinations = {
    'BUD': 'Budapest',
    'CMN': 'Casablanca',
    'IST': 'Istanbul'
}


class AssertionError(Exception):
    def __init__(self, destination):
        self.destination = destination

    def __str__(self):
        return 'Sorry, Small World currently does not fly to this destination!'


print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below:
assert destination in destinations, AssertionError(destination)

print('Great! Retrieving information for your flight to ...' + city_name)
