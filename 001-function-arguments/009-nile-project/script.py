from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:


def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    # slow way
    # from_lat = from_coords[0]
    # from_long = from_coords[1]
    # to_lat = to_coords[0]
    # to_long = to_coords[1]
    # distance = get_distance(from_lat, from_long, to_lat, to_long)

    # efficient way
    distance = get_distance(*from_coords, *to_coords)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance*shipping_rate
    return format_price(price)


# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here

# Test the function by calling
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling
# test_function(calculate_money_made)
