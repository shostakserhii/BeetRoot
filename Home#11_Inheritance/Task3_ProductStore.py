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
#        if identifier_type == 'name':
        for v in self.base.values():
            if v[0].name == self.identifier:
                v[0].price*=1-(self.percent/100)
        print(self.base)  


    def __str__(self):
        return self.base

    def __repr__(self):
        return self.base

ball = Product("Sport", "Ball", 100)

store = ProductStore()
store.add(ball, 10)
fitball = Product("Sport", "Fitball", 90)
store.add(fitball,20)
store.set_discount('Ball', 10, 'name')
store.set_discount('Ball', 10, 'type')
