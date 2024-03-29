import random as rd

class Restaurant:
    def __init__(self):
        self.name = name
        self.menu = menu

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item, price in self.menu.items():
            print(f"(${price}) {item}")

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
    area_delivery_costs = {1: 2, 2: 2.5, 3: 2.5, 4: 2.5, 5: 2.5}
    if area in area_delivery_costs:
        delivery_cost = round(area_delivery_costs[area]*traffic_coefficient, 2)
        print("")
        print(f"Delivery cost: ${delivery_cost:.2f}")
    else:
        print("Invalid area number.")
         
                
def calculate_delivery_time(area):
    area_delivery_times = {1: 10, 2: 15, 3: 25, 4: 30, 5: 20}
    if area in area_delivery_times:
        delivery_time = int(area_delivery_times[area] * traffic_coefficient)
        print("")
        print(f"Estimated delivery time: {delivery_time} min due to {traffic_type}.")

    else:
        print("Invalid area number.")

          
          
def main():
    restaurants = [CheesecakeFactory(), McDonalds(), TatteBakery(), DominosPizza(), Subway(), Chipotle()]
    print("Restaurants:")
    for index, restaurant in enumerate(restaurants, start=1):
        print(f"{index}. {restaurant.name}")

    choice = int(input("Choose a restaurant by number: ")) - 1
    print()
    chosen_restaurant = restaurants[choice]

    print("____________________________________________________________________")
    print("")
    chosen_restaurant.display_menu() 
    print("____________________________________________________________________")
    
    
    #ask user for items
    #calculate cost
    
    print("")
    print("1. Fennway")
    print("2. Newbury")
    print("3. Downtown")
    print("4. Seaport")
    print("5. Backbay")
    print("")
    area_number = int(input("Please enter your area number:")) 
    print("____________________________________________________________________")
    

    
    #Output invoice
    print("")
    print(f"Invoice:")
    
    print("")
    print("ITEM LIST HERE") #update item list
    print("")
    
    calculate_delivery_cost(area_number)
    
    calculate_delivery_time(area_number)

    
    
main()





