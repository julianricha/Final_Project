import random as rd

class Restaurant:
    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item, price in self.menu.items():
            print(f"(${price}) {item}")
            
    def order_item(self, choice):
        # To-do
        pass

class CheesecakeFactory(Restaurant):
    def __init__(self):
        # Simple menu - choose any item(s) you want
        menu = {"Oreo Cheesecake": (7,450), 
                "Strawberry Cheesecake": (6,400),
                "Burger Spring Rolls": (10,300),
                "Caesar Salad": (8,200),
                "Tomato Pasta": (11,270),
                "Fillet Mignon Steak": (20,300)}
        
        super().__init__(menu)

    # User simply chooses from menu, calculates price and calories for each

class McDonalds(Restaurant):
    def __init__(self, size, sandwich, drink):
        self.size = size
        self.sandwich = sandwich
        self.drink = drink
        
    meal_price = {"Happy Meal": 10, "Regular Meal": 14, "Large Meal": 18}
    meal_calories = {"Happy Meal": 500, "Medium Meal": 790, "Large Meal": 1100}
    meal_sandwich_calories = {"Big Mac": 450, "Quarter Pounder": 500, "McChicken": 350, "Cheese Burger": 300}
    def __init__(self):
        # Compound menu - choose either sandwich or sandwich + meal
        meal_menu = {"Happy Meal": (3, 500), "Regular Meal": (5, 790), "Large Meal": (8, 1100)}
        sandwich_menu = {"Big Mac": (6, 450), "Quarter Pounder": (5, 500), "McChicken": (3, 350), "Cheese Burger": (3, 300)}
        
        menu = {"meals": meal_menu, "sandwiches": sandwich_menu}
        
        super().__init__(menu)
       
    # User chooses meal size between happy meal, regular, and large, each with a price to start
    # User chooses sandwich type with specific price and calorie count
    # Calories for all drink are same, and already included in meal_calories along with fry calories
    
class TatteBakery(Restaurant):
    def __init__(self):
        # Add $1 and 100 calories for each additional option on each item
        # When ordering, user must be prompted for each option - either "Y" or "N"
        menu = {"Almond Croissant": (3,400, ("butter", "egg")),
                    "Short Ribs Sandwich": (10,560, ("meat", "onions")),
                     "Chicken Pita": (8,450, ("toasted", "pickles")),
                     "Coffee": (2, 100, ("iced", "almond milk")),
                     }
        super().__init__(menu)
        
class DominosPizza(Restaurant): 
    def __init__(self):
        # User must choose a size and a choice
        size_menu = {"Small": (10, 500), "Medium": (13, 750), "Large": (16, 900)}
        choice_menu = {"Cheese": (2, 200), "Pepperoni": (5, 250), "Hawaiian": (3, 200), "Veggie": (4, 170), "BBQ Chicken": (6, 350)}
        
        menu = {"size": size_menu, "choice": choice_menu}
        
        super().__init__(menu)
            
    # User chooses size with each size having specific number of calories and price
    # User chooses type of pizza from list of above that adds a specific amount extra to the price based on choice along with specific calorie count 
    # Calculates total cost and total calories based on choice of size and pizza

class Subway(Restaurant):#To edit later customisable subs size
    def __init__(self):
        bread = {"6 inch": (5,200), "12 inch": (10,400)}
        protein = {"Turkey": (5,300),"Chicken": (4,200),"Tuna": (7,320), "Steak": (8,230), "Meatball": (6,300)}
    
        menu = {"Bread Size": bread, "Protein": protein}
        super().__init__(menu)
    
    # User chooses between 6 and 12 inch bread each with price and calorie count, PRICE ONLY ACCOUNTS FOR BREAD SIZE AND PROTEIN, 
    # User adds protein with specific calorie count, doubles for 12 inch
    # User adds toppings only with price count

class Chipotle(Restaurant): #To edit later customisable bowl
    def __init__(self):
        
        choice = {"Burrito": (8,120), "Bowl": (6,100)}
        rice = {"White Rice": (), "Brown Rice": ()}
        protein = {"Carne Asada": (6,250),"Chicken Pastor": (4,300),"Barbacoa": (5,330)}
        toppings = {"Guac": (3,200),"Sour Cream": (2,100),"Corn": (2,70), "Pico Gallo": (3,60), "Hot Sauce": (1,20)}
        
        menu = {"Burrito or Bowl": choice, "White or Brown Rice": rice, "Protein": protein, "Toppings": toppings}
        super().__init__(menu)
    
    # User builds either bowl or burrito from scratch by choosing an option from each category while knowing both price and calorie count
  

traffic_dict = {"no traffic": 1, "low traffic": 1.1, "high traffic": 1.3}
traffic_type, traffic_level = rd.choice(list(traffic_dict.items()))
    
def calculate_delivery_cost(area):
    area_delivery_costs = {1: 2, 2: 2.5, 3: 2.5, 4: 2.5, 5: 2.5}
    if area in area_delivery_costs:
        delivery_cost = round(area_delivery_costs[area]*traffic_level, 2)
        print("")
        print(f"Delivery cost: ${delivery_cost:.2f}")
    else:
        print("Invalid area number.")
         
                
def calculate_delivery_time(area):
    area_delivery_times = {1: 10, 2: 15, 3: 25, 4: 30, 5: 20}
    if area in area_delivery_times:
        delivery_time = int(area_delivery_times[area] * traffic_level)
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
    
    
    def order_cart()
    # for next iteration
    def calculate_total_cost():
    # for next iteration
    
   
    
    
    print("")
    print("1. Fenway")
    print("2. Newbury")
    print("3. Downtown")
    print("4. Seaport")
    print("5. Backbay")
    print("")
    area_number = int(input("Please enter your area number:")) 
    print("____________________________________________________________________")
    

    
    
    print("")
    print(f"Invoice:")
    
    print("")
    print("ITEM LIST HERE") 
    print("")
    
    calculate_delivery_cost(area_number)
    
    calculate_delivery_time(area_number)

    
    
main()





