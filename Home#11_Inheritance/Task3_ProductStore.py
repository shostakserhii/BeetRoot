import json

class Product():

    def __init__(self, name, type,  price, amount = 0):
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
    income = 0

    def __init__(self):
        pass

    def add(self, product, amount): 
        product.price *= 1.3
        self.amount = amount
        self.base.append(product)

    def set_discount(self, identifier, percent, identifier_type):
        for item in self.base:
            if getattr(item, identifier_type) == identifier:
                item.price *= 1-(int(percent)/100)
                print(f"New price of {item.name} is: {item.price}.")
        else:
            return "No product found"

    def sell_product(self, product_name, amount):
        for item in self.base:
            if item.name == product_name:
                if item.amount < amount:
                    raise ValueError("Not sufficient amount available! ")
                item.amount -= amount
                self.income += (item.price * (amount))
                print(f"{amount}  {product_name} = {item.price * (amount)}")

    def get_income(self):
        return f"""
            Total income = {self.income}
            Profit = {self.income*0.7}
        """
    
    def base_show(self):
        i = 0
        for product in self.base:
            i += 1
            print(f"""Product #{i}

            Type:   {product.type}
            Name:   {product.name}
            Price:  {product.price}
            Amount: {product.amount}
            """)

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

        Operations:
            a - Add product
            d - Set disount
            s - Sell product amount
            i - Show income
            b - Show All Products

        q - quit
        make your choice    """) 
        if choice.strip().lower() == 'q':
            print("Chao")
            break
        if choice.strip().lower() == 'a':
            name = input("Name: ").strip().lower()
            if name.isalpha() != True:
                raise ValueError("Error: 'Name' should consist of alphabet symbols")
            type = input("Type: ").strip().lower()
            if type.isalpha() != True:
                raise ValueError("Error: 'Type' should consist of alphabet symbols")
            price = input("Price: ")
            if isinstance(price, int) != True:
                raise ValueError("Error: 'Price' should be integer ")    
            amount = int(input("Amount: "))
            if isinstance(amount, int) != True:
                raise ValueError("Error: 'Amount' should be integer ")   
            store.base.append(Product(name,type,price,amount))
        if choice.strip().lower() == 'd':
            identifier_type = input("""To assign discount to single product put:
                    - name
            for the type of products put:
                    - type
                    """).strip().lower()
            identifier = input("Type title/Product name: ").strip().lower()
            discount = input("Size of the discount: ")
            store.set_discount(identifier, discount, identifier_type)
        if choice.strip().lower() == 's':
            name = input("Product name: ").strip().lower()
            amount = int(input("Amount: "))
            store.sell_product(name, amount)
        if choice.strip().lower() == 'i':
            store.get_income()
        if choice.strip().lower() == 'b':
            store.base_show()
        else:
            print("No operation/product found")
        continue

    store.base = [Product.convert(item) for item in store.base]
    print(store.base)
    with open('product_base','w') as product_base:
        json.dump(store.base, product_base, indent=4)
except ValueError as e:
    print(f"Something went wrong...oops. More details here -> {e}")
    raise ValueError 
finally: 
    print("Closing app")