instrument_prices = {
    'Banjo': 200,
    'Cello': 1000,
    'Flute': 100,
}


def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price * discount_percentage)
    print("The instrument's discounted price is: " + str(discounted_price))


instrument = 'Clarinet'
discount = '20'

# Write your code below:

display_discounted_price(instrument, discount)
