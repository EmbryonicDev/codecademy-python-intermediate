sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
print(dir(sku_list))
sku_iterator_object_one = iter(sku_list)
sku_iterator_object_two = sku_list.__iter__()

print("-----------------------------")
print(sku_iterator_object_one)
print(sku_iterator_object_two)
