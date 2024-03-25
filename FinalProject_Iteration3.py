#!/usr/bin/env python
# coding: utf-8

# In[24]:


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

        
#def calculate_delivery_cost_and_time()
        

def main():
    restaurants = [CheesecakeFactory(), McDonalds(), TatteBakery(), DominosPizza(), Subway(), Chipotle()]
    print("Restaurants:")
    for index, restaurant in enumerate(restaurants, start=1):
        print(f"{index}. {restaurant.name}")

    choice = int(input("Choose a restaurant by number: ")) - 1
    print()
    chosen_restaurant = restaurants[choice]

    chosen_restaurant.display_menu() 
    
    
#ask user for items
#ask user for location
#calculate total cost = sum items + delivery cost
#Output invoice and delivery ETA (implement random for trafic)

main()


# In[ ]:





# In[ ]:




