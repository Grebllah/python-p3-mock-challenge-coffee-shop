class Coffee:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
    
    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customers = [order.customer for order in Order.all if order.coffee == self]
        unique_customers = set(customers)
        return [customer for customer in unique_customers]
    
    def num_orders(self):
        orders = [order for order in Order.all if order.coffee == self]
        return len(orders)
    
    def average_price(self):
        sum = 0
        prices = [order.price for order in Order.all if order.coffee == self]
        print(prices)
        for price in prices:
            sum += price
        print(sum)
        return sum / len (prices)

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and len(name) <= 15 and len(name) >= 2:
            self._name = name
    
    name = property(get_name, set_name)
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffees = [order.coffee for order in Order.all if order.customer == self]
        uniques = set(coffees)
        return [coffee for coffee in uniques]
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    def get_price(self):
        return self._price

    def set_price(self, price):
            if not hasattr(self, "price"):
                self._price = price
    
    price = property(get_price, set_price)