class Product():

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'{self.type, self.name, self.price}'
    
    def __repr__(self):
        return f'{self.type, self.name, self.price}'

class ProductStore():

    base = {}
    profit = 0

    def __init__(self):
        pass

    def add(self, product, amount):
        self.product = product
        self.amount = amount
        product.price *= 1.3
        self.base[product.name] = product,amount    
        print(self.base)

    def set_discount(self, identifier, percent, identifier_type):
        self.identifier = identifier
        self.percent = percent
        self.identifier_type = identifier_type
        if identifier_type == 'name':
            for v in self.base.values():
                if v[0].name == self.identifier:
                    v[0].price *= 1-(self.percent/100)
        if identifier_type == 'type':
            for v in self.base.values():
                if v[0].type == self.identifier:
                    v[0].price *= 1-(self.percent/100)
        print(self.base)

    def sell_product(self, product_name, amount):
        self.product_name = product_name
        self.amount = amount
        for v in self.base.values():
            if v[0].name == self.product_name:
                if v[1]<self.amount:
                    return "insufficient ammount, sorry"
                income = (v[1] - self.amount)*v[0].price
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

ball = Product("Sport", "Ball", 100)
try:
    store = ProductStore()
    store.add(ball, 10)
    fitball = Product("Sport", "Fitball", 90)
    store.add(fitball,20)
    store.set_discount('Ball', 10, 'name')
    store.set_discount('Sport', 10, 'type')
    print(store.sell_product('Fitball', 10))
    print(store.get_income())
    store.show_products()
    print(store.get_product_info("Ball"))
except Exception as e:
    print(f"Something went wrong...oops. More details here -> {e}")
    raise ValueError 
finally: 
    print("Closing app")