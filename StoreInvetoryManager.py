import json
def remove(x):
    Products.remove(x)
def add(x):
    Products.append(x)
with open("products.json") as meu_json:
    data = json.load(meu_json)
Products = data
# Change 'Store's Stock' to the name of your store
print("Store's Stock.")
print(Products)
print("Commands: Use 'save' to save your edited list, 'close' to close the app, 'list' to see the list,'add' to add the product and 'remove' to remove the product.")
while True:
    choice1 = input("What do you want to do? -> ")
    if choice1 == 'add':
        add1 = input("Product name -> ")
        add(add1)
        print(add1, "has been added.")
        print(Products)
        continue
    elif choice1 == "remove":
        remove1 = input("Product to remove -> ")
        remove(remove1)
        print(remove1, "has been removed.")
        print(Products)
        continue
    elif choice1 == "list":
        print(Products)
        continue
    elif choice1 == 'save':
        products_json = open("products.json", "w")
        products_json.write(json.dumps(Products, sort_keys=True, indent=4))
        products_json.close()
        print("The product list has been saved.")
        continue
    elif choice1 == 'close':
        break
