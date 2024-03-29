import random as rd

class Restaurant:
    def __init__(self, name, menu, calories):
        self.name = name
        self.menu = menu
        self.calories = calories

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item, price in self.menu.items():
            print(f"(${price}) {item}")

class CheesecakeFactory(Restaurant):
    def __init__(self, choice):
        self.choice = choice
    
    menu_price = {"Oreo Cheesecake": 7, 
                     "Strawberry Cheesecake": 6,
                     "Burger Spring Rolls": 10,
                     "Caesar Salad": 8,
                     "Tomato Pasta": 11,
                     "Fillet Mignon Steak": 20}
    
    menu_calories = {"Oreo Cheesecake": 450, 
                     "Strawberry Cheesecake": 400,
                     "Burger Spring Rolls": 300,
                     "Caesar Salad": 200,
                     "Tomato Pasta": 270,
                     "Fillet Mignon Steak": 300}
    # User simply chooses from menu, calculates price and calories for each

class McDonalds(Restaurant):
    def __init__(self, size, sandwich, drink):
        self.size = size
        self.sandwich = sandwich
        self.drink = drink
        
    meal_price = {"Happy Meal": 10, "Regular Meal": 14, "Large Meal": 18}
    meal_calories = {"Happy Meal": 400, "Medium Meal": 620, "Large Meal": 850}
    meal_sandwich_calories = {"Big Mac": 450, "Quarter Pounder": 500, "McChicken": 350, "Cheese Burger": 300}
    meal_drink_calories = {"Happy Meal": 100, "Regular Meal": 170, "Large Meal": 250}

    # User chooses meal size between happy meal, regular, and large, each with a price to start
    # User chooses sandwich type with specific price and calorie count
    # Calories for all drink are same, and already included in meal_calories along with fry calories
    
class TatteBakery(Restaurant):
    def __init__(self):
        self.menu = {"Croissant": 3,
                     "Coffee": 2,
                     "Sandwich": 7, 
                     "Salad": 8,
                     "Quiche": 9}
        
        # User simply chooses from menu 

class DominosPizza(Restaurant): 
    def __init__(self, size, choice, toppings):
        self.size = size
        self.choice = choice
        self.toppings = toppings
        
        menu = {"Margherita": 10, 
                     "Pepperoni": 12, 
                     "Hawaiian": 11, 
                     "Veggie": 10, 
                     "BBQ Chicken": 14}
        
    pizza_size_price = {"Small": 10, "Medium": 13, "Large": 16}
    pizza_choice_price = {"Cheese": 2, "Pepperoni": 5, "Hawaiian": 3, "Veggie": 4}
    pizza_size_calories = {"Small": 500, "Medium": 750, "Large": 900}
    pizza_choice_calories = {"Cheese": 100, "Pepperoni": 250, "Hawaiian": 200, "Veggie": 170}
        
    # User chooses size with each size having specific number of calories and price
    # User chooses type of pizza from list of above that adds a specific amount extra to the price based on choice along with specific calorie count 
    # Calculates total cost and total calories based on choice of size and pizza

class Subway(Restaurant):#To edit later customisable subs size
    def __init__(self, bread, protein, toppings):
        self.bread = bread
        self.protein = protein
        self.toppings = toppings
        
    
    bread_price = {"6 inch": 5, "12 inch": 10}
    bread_calories = {"6 inch": 100, "12 inch": 200}
    protein_price = {"Turkey": 5,"Chicken": 4,"Tuna": 7, "Steak": 8, "Meatball": 6}
    protein_calories = {"Turkey": 200,"Chicken": 150,"Tuna": 320, "Steak": 230, "Meatball": 300}
  
    # User chooses between 6 and 12 inch bread each with price and calorie count, PRICE ONLY ACCOUNTS FOR BREAD SIZE AND PROTEIN, 
    # User adds protein with specific calorie count, doubles for 12 inch
    # User adds toppings only with price count

class Chipotle(Restaurant): #To edit later customisable bowl
    def __init__(self, meal, protein, toppings, extras):
       self.choice = choice
       self.protein = protein
       self.toppings = toppings
       self.extras = extras
       
    
    choice_calories = {"Burrito": 120, "Bowl": 100}
    protein_calories = {"Carne Asada": 250,"Chicken Pastor": 300,"Barbacoa": 330,}
    toppings_calories = {"Guac": 200,"Sour Cream": 100,"Corn": 70, "Pico Gallo": 60, "Hot Sauce":20}
    
    choice_price = {"Burrito": 8, "Bowl": 6}
    protein_price = {"Carne Asada": 250,"Chicken Pastor": 300,"Barbacoa": 330,}
    toppings_price = {"Guac": 3,"Sour Cream": 2,"Corn": 2, "Pico Gallo": 3, "Hot Sauce":1}
    
    
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





