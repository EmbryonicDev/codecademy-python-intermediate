from print_checkpoint import print_checkpoint

print_checkpoint(1)
company_name = 'Soul Stitching'
print('company_name printed:\n', company_name)

print_checkpoint(2)
company_location = (29.9792458, 31.1342515)
print('company_location printed:\n', company_location)

print_checkpoint(3)
company_products = ['shirt', 'trousers', 'shorts', 'hat', 'towel']
print('company_products printed:\n', company_products)

print_checkpoint(4)
company_data = {}
for x in [('name', company_name), ('location', company_location), ('products', company_products)]:
    company_data[x[0]] = x[1]
print('company_data printed:\n', company_data)
