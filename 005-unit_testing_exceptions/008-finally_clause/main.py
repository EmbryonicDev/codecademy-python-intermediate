import database

instrument = 'Synthesizer'
database.connect_to_database()

try:
    database.display_instrument_info(instrument)
except KeyError:
    print('Oh no! This instrument does not exist.')
else:
    print(instrument)
# Write your code below:
