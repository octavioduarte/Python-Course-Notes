# https://github.com/luizomf/cursopython2023/commit/343371a72ef869664060287b11ce59b3388336c1
import copy

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]


new_products = copy.deepcopy(products)

new_products = [ {**x, 'price': round(x['price'] * 1.10, 2) } for x in new_products]

new_products.sort(key= lambda x: x["price"])

print(*new_products, sep='\n')