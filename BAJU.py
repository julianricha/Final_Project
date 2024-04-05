import random as rd

class Restaurant:
    def __init__(self):
        self.name = name
        self.menu = menu

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for index, (item, price) in enumerate(self.menu.items(), start=1):
            print(f"{index}. (${price}) {item}")

class CheesecakeFactory(Restaurant):
    def __init__(self):
        self.name = "Cheesecake Factory"
        self.menu = {"Cheesecake": 7, 
                     "Burger": 10,
                     "Salad": 8,
                     "Pasta": 11,
                     "Steak": 15}

class McDonalds(Restaurant):
    def __init__(self):
        self.name = "McDonalds"
        self.menu = {"Big Mac": 5,
                     "Fries": 2, 
                     "Chicken Nuggets": 4, 
                     "McFlurry": 3, 
                     "Quarter Pounder": 5}

class TatteBakery(Restaurant):
    def __init__(self):
        self.name = "Tatte Bakery"
        self.menu = {"Croissant": 3,
                     "Coffee": 2,
                     "Sandwich": 7, 
                     "Salad": 8,
                     "Quiche": 9}

class DominosPizza(Restaurant): #To edit later customisable pizza size and toppings
    def __init__(self):
        self.name = "Domino's Pizza"
        self.menu = {"Margherita": 10, 
                     "Pepperoni": 12, 
                     "Hawaiian": 11, 
                     "Veggie": 10, 
                     "BBQ Chicken": 14}

class Subway(Restaurant):#To edit later customisable subs size
    def __init__(self):
        self.name = "Subway"
        self.menu = {"Turkey Sub": 8, 
                     "Veggie Delight": 7, 
                     "Meatball Marinara": 9, 
                     "Tuna": 8, 
                     "Steak & Cheese": 10}

class Chipotle(Restaurant): #To edit later customisable bowl
    def __init__(self):
        self.name = "Chipotle"
        self.menu = {"Burrito": 9, 
                     "Bowl": 8, 
                     "Tacos": 7, 
                     "Salad": 8, 
                     "Quesadilla": 10}

    

traffic_dict = {"no traffic": 1, "low traffic": 1.1, "high traffic": 1.3}
traffic_type, traffic_coefficient = rd.choice(list(traffic_dict.items()))

def calculate_delivery_cost(area):
    area_delivery_costs = {1: 2, 2: 2.5, 3: 3, 4: 3.5, 5: 4}
    if area in area_delivery_costs:
        return round(area_delivery_costs[area] * traffic_coefficient, 2)
    else:
        print("Invalid area number.")
        return 0

def calculate_delivery_time(area):
    area_delivery_times = {1: 10, 2: 15, 3: 25, 4: 30, 5: 20}
    if area in area_delivery_times:
        delivery_time = int(area_delivery_times[area] * traffic_coefficient)
        print(f"Estimated delivery time: {delivery_time} min due to {traffic_type}.")
    else:
        print("Invalid area number.")

def main():
    restaurants = [CheesecakeFactory(), McDonalds(), TatteBakery(), DominosPizza(), Subway(), Chipotle()]
    print("Restaurants:")
    for index, restaurant in enumerate(restaurants, start=1):
        print(f"{index}. {restaurant.name}")

    choice = int(input("Choose a restaurant by number: ")) - 1
    chosen_restaurant = restaurants[choice]

    print("____________________________________________________________________")
    chosen_restaurant.display_menu() 
    order = input("Enter the items you want to order, separated by a comma: ").split(',')
    print("____________________________________________________________________")
    
    
    order = [item.strip() for item in order]  # Clean whitespace

    order_items = {item: chosen_restaurant.menu[item] for item in order if item in chosen_restaurant.menu}
    if not order_items:
        print("No valid items were ordered.")
        return

    print("")
    print("1. Fennway")
    print("2. Newbury")
    print("3. Downtown")
    print("4. Seaport")
    print("5. Backbay")
    print("")
    
    area_number = int(input("Please enter your area number: "))
    delivery_cost = calculate_delivery_cost(area_number)

    print("____________________________________________________________________")
    print("Invoice:")
    print("")
    total_cost = 0
    for item, price in order_items.items():
        print(f"{item}: ${price}")
        total_cost += price

    print(f"Delivery cost: ${delivery_cost}")
    total_cost += delivery_cost
    print("")
    print(f"Total cost: ${total_cost}")
    print("")
    calculate_delivery_time(area_number)
    print("")
    print("Thank you for odering with BAJU delivery app!")
main()


