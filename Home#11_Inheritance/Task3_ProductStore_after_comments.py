class Product():

    def __init__(self, type, name, price):
                self.type = type
                self.name = name
                self.price = price

    def __str__(self):
        return f'{self.type, self.name, self.price}'
    
    def __repr__(self):
        return f'{self.type, self.name, self.price}'


def save_to_ProductStore (obj, amount = 0):
        if obj.name.isalpha() != True:
            raise ValueError("The error: 'Name' should consist of alphabet symbols")
        if obj.type.strip().isalpha() != True:
            raise ValueError("The error: 'Type' should consist of alphabet symbols")
        if isinstance(obj.price, int) != True:
            raise ValueError("The error: 'Price' should consist of digits")    
        else:
            ProductStore.base[obj.name]=obj, amount
    

class ProductStore():

    base = {}
    profit = 0

    def __init__(self):
        pass

    def add(self, product, amount): 
        product.price *= 1.3
        self.base[product.name] = product,amount

    def set_discount(self, identifier, percent, identifier_type):
        self.identifier = identifier
        self.percent = percent
        self.identifier_type = identifier_type
        for v in self.base.values():
            if getattr(v[0], self.identifier_type) == self.identifier:
                v[0].price *= 1-(self.percent/100)



    def sell_product(self, product_name, amount):
        income = 0
        for v in self.base.values():
            if v[0].name == product_name:
                if v[1]<amount:
                    raise ValueError("insufficient ammount, sorry")
                income = (v[1] - amount)*v[0].price
        self.profit += income
        return f"Income is: {income}"

    def get_income(self):
        return f"Total profit is {self.profit}, pure profit is {self.profit*0.3}"

    def show_products(self):
        for v in self.base.values():
            print(f"""Name:{v[0].name}
                Type: \t{v[0].type}
                Price: \t{v[0].price}
                Available Amount: {v[1]}
            """)

    def get_product_info(self, product_name):
        self.product_name = product_name
        for v in self.base.values():
            if v[0].name==self.product_name:
                return (f"{v[0].name}, {v[1]}")

    def __str__(self):
        return self.base

    def __repr__(self):
        return self.base

try:
    cpu = Product("PC", "CPU", 111)
    save_to_ProductStore(cpu)
    ball = Product("Sport", "Ball", 100)
    store = ProductStore()
    store.add(ball, 10)
    fitball = Product("Sport", "Fitball", 150)
    store.add(fitball,20)
    store.set_discount('Ball', 10, 'name')
    store.set_discount('Sport', 10, 'type')
    print(store.sell_product('Fitball', 10))
    print(store.get_income())
    store.show_products()
    print(store.get_product_info("Ball"))
    print(store.base)
except ValueError as e:
    print(f"Something went wrong...oops. More details here -> {e}")
    raise ValueError 
finally: 
    print("Closing app")