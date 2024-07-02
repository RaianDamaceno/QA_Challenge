def sort_products(products, sort_key, ascending=True):
    copy_list = products[:]

    for i in range (len(copy_list)):
        for j in range(0, len(copy_list)-i-1):
            if(ascending and copy_list[j][sort_key] > copy_list[j+1][sort_key]) or (not ascending and copy_list[j][sort_key] < copy_list[j+1][sort_key]):
                temp = copy_list[j]
                copy_list[j] = copy_list[j+1]
                copy_list[j+1] = temp

    return copy_list     

products = [
    {"name": "Product A", "price": 100, "stock": 5},
    {"name": "Product B", "price": 200, "stock": 3},
    {"name": "Product C", "price": 50, "stock": 10},
    {"name": "Product D", "price": 70, "stock": 11},
    {"name": "Product E", "price": 50, "stock": 22}
]

sorted_products = sort_products(products, "price", ascending=False)

for product in sorted_products:
    print(product)