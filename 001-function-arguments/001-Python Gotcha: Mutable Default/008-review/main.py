tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'reserved': True,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes',
            'total': [534.50, 20.0, 5]
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def assign_table(table_number, name, vip_status=False, reserved=True):
    text = ""
    table_len = len(tables[table_number])
    if table_len < 1:
        tables[table_number]['name'] = name
        tables[table_number]['vip_status'] = vip_status
        tables[table_number]['reserved'] = reserved
        tables[table_number]['order'] = {}
        print(f"Table {table_number} has been assigned to {name}")
    else:
        if tables[table_number]['reserved']:
            if table_len > 2:
                text = f"Table {table_number} is currently in use. please assign a different table, or use remove_guest({table_number}) to clear the table first"
            else:
                text = f"Table {table_number} has been reserved, please book a different table."

    frame = "-"*len(text)
    print(f"{frame}\n{text.upper()}\n{frame}")


def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks
    print(f"Table {table_number}'s order has been updated.")


def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(f"Each person needs to pay: ${split_price}")


def get_table_total(table_number):
    pre_total = tables[table_number]['order']['total']
    total_tip = pre_total[0] * (pre_total[1]/100)
    total = pre_total[0]+total_tip
    print(f"The total cost for table {table_number} = ${total}")


def clear_table(table_number):
    tables[table_number] = {}
    print(f"Table {table_number} has been cleared.")


def remove_order_item(table_number, **items_to_remove):
    ordered_food = tables[table_number]['order']['food_items'].split(", ")
    ordered_drinks = tables[table_number]['order']['drinks'].split(", ")

    food_to_cancel = items_to_remove.get('food').split(", ")
    drinks_to_cancel = items_to_remove.get('drinks').split(", ")

    for item in food_to_cancel:
        if item in ordered_food:
            ordered_food.remove(item)

    for item in drinks_to_cancel:
        if item in ordered_drinks:
            ordered_drinks.remove(item)

    new_food = ", ".join(ordered_food)
    new_drinks = ", ".join(ordered_drinks)

    print(f"Removing order items from table {table_number}")
    assign_food_items(table_number, food=new_food, drinks=new_drinks)


def reserve_table(table_number):
    tables[table_number]['reserved'] = True
    print(f"Table {table_number} has been reserved.")


# Testing ##################\
if __name__ == '__main__':
    get_table_total(1)

    calculate_price_per_person(*tables[1]['order']['total'])

    assign_table(2, 'Steve')

    assign_food_items(2, food='Seabass, Gnocchi, Pizza',
                      drinks='Margarita, Water, Beer')

    remove_order_item(2, food='Gnocchi', drinks='Water, Beer')

    reserve_table(3)

    assign_table(2, 'Sally')

    assign_table(3, 'Sally')

    clear_table(3)

    assign_table(3, 'Sally')

    print(tables)
