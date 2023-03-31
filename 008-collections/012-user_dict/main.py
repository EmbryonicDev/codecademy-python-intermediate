from collections import UserDict

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
# Checkpoint 1


class OrderProcessingDict(UserDict):

    def clean_orders(self):
        processed_orders = []
        for k, v in self.items():
            if v['order_status'] == 'complete':
                # if v.get('order_status') == 'complete':
                processed_orders.append(k)
        for k in processed_orders:
            del self.data[k]


process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)
