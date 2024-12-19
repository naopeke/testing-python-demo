class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self): # debugger
        return f"<Person({self.name}, {self.age})>"
    
bob = Person("Bob", 35)
print(bob)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
    
    def stock_price(self):
        return sum([item['price'] for item in self.items])
        '''
        total = 0
        for item in self.items:
            total += item['price']
        return total
        '''
store = Store("My Store")
store.add_item("Apple", 1.5)
store.add_item("Banana", 0.8)
print(store.stock_price())  # Output: 2.3
