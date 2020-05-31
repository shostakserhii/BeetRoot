import json

class Product():

    def __init__(self, name, type,  price, amount = None):
                self.name = name
                self.type = type
                self.price = price
                self.amount = amount

    def __str__(self):
        return f'{self.name, self.type, self.price, self.amount}'
    
    def __repr__(self):
        return f'{self.name, self.type, self.price, self.amount}'
    
    def convert(self):
        return {
            'name':self.name,
            'type':self.type,
            'price':self.price,
            'amount':self.amount
        }


class ProductStore():

    base = []
    profit = 0

    def __init__(self):
        pass

    def add(self, product, amount): 
        product.price *= 1.3
        self.amount = amount
        self.base.append(product)

    def set_discount(self, identifier, percent, identifier_type):
        self.identifier = identifier
        self.percent = percent
        self.identifier_type = identifier_type
        pass

    def sell_product(self, product_name, amount):
        #income = 0
        pass

    def get_income(self):
        pass

    def show_products(self):
        pass

    def get_product_info(self, product_name):
        pass
    def __str__(self):
        return self.base

    def __repr__(self):
        return self.base

store = ProductStore()
try:
    json_file = open('product_base')
    product_base = json.load(json_file)
    for item in product_base:
        store.base.append(Product(**item))
except json.decoder.JSONDecodeError:
    store.base=[]
json_file.close()



try:
    while True:
        choice = input(f"""
        product_base file was successfuly loaded...

        Operations:
            a - Add product
            d - Set disount
            s - Sell product amount
            i - Show income

        q - quit
        make your choice    """) 
        if choice.strip().lower() == 'q':
            print("Chao")
            break
        if choice.strip().lower() == 'a':
            name = input("Name: ")
            type = input("Type: ")
            price = input("Price: ")
            amount = input("Amount: ")
            store.base.append(Product(name,type,price,amount))
        if choice.strip().lower() == 'd':
            identifier_type = input("Do you want to assign discount to single product or for the type of products? Put type/name: ")
            identifier = input("Type title/Product name: ")
            discount 
#    cpu = Product("CPU", "PC", 111)
    
#    store.add(cpu, 10)
    print(store.base)

    store.base = [Product.convert(item) for item in store.base]
    print(store.base)
    with open('product_base','w') as product_base:
        json.dump(store.base, product_base, indent=4)
except ValueError as e:
    print(f"Something went wrong...oops. More details here -> {e}")
    raise ValueError 
finally: 
    print("Closing app")