"""
Hi! This is the seventh lab
"""


class Item:
    """
    Describes the item
    >>> my_items2 = Item('flowers',11)
    >>> my_items2.__str__()
    The price of flowers is 11 dollars.
    """
    def __init__(self, name, price):
        """
        param name: str
        param price: float
        return: None
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        return: str
        """
        print(f'The price of {self.name} is {self.price} dollars.')


class Location:
    """
    Describes location of the user
    """
    def __init__(self, city, postoffice):
        """
        param city: str
        param postoffice: int
        """
        self.city = city
        self.postoffice = postoffice


class Vehicle:
    """
    Gives info about vehicles
    """
    def __init__(self, vehicleNo, isAvailable=True):
        """
        param vehicleNo: int
        param isAvailable: bool
                """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order:
    """
    Set order
    # This doctest is possible of u don't call the function with the arguments, because each time it generates/
    a new number
    # >>> my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]; \
    # my_order2 = Order('Ivan', 'Lviv',my_items2); my_order2.__str__()
    # Your order number is 1001
    """
    def __init__(self, user_name, location: Location, items, vehicle=None):
        """
        param order: int
        param user_name: str
        param location: object
        param items: list
        param vehicle: None
        return: None
        """
        self.orderId = Order.__generateOrderNumber()
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    __lastOrderNumber = 1000   #Here the user can change the initial number of order

    @classmethod
    def __generateOrderNumber(cls):
        Order.__lastOrderNumber += 1
        return Order.__lastOrderNumber

    def __str__(self):
        print(f'Your order number is {self.orderId}')

    def calculateAmount(self):
        return len(self.items)

    def assignVehicle(self, vehicle=Vehicle):
        self.vehicle = vehicle

    def calculate_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price


class LogisticSystem:
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order=Order):
        """
        Discover if the available vehicle exists
        """
        isVehicleFound = False
        for element in self.vehicles:
            if element.isAvailable:
                self.orders.append(order)
                order.assignVehicle(element)
                element.isAvailable = False
                isVehicleFound = True
                break
        if not isVehicleFound:
            print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderId):
        """
        Returns the info about order
        """
        isOrderFound = False
        for element in self.orders:
            if orderId == element.orderId:
                print(f'Your order #{orderId} is sent to {element.location}. Total price: {element.calculate_price()} UAH.')
                isOrderFound = True
                break
        if not isOrderFound:
            print('No such order')


# vehicles = [Vehicle(1), Vehicle(2)]
# logSystem = LogisticSystem(vehicles)
# my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
# my_order2 = Order('Ivan', 'Lviv',my_items2)
# logSystem.placeOrder(my_order2)
# logSystem.trackOrder(my_order2.orderId)
# my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
# my_order3 = Order('Olesya', 'Kharkiv', my_items3)
# logSystem.placeOrder(my_order3)
# logSystem.trackOrder(my_order3.orderId)