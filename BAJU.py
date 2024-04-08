import random as rd

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        
    def print_order_summary(self, cart, total_price, total_calories):
        print("Order summary: ")
        for i, item in enumerate(cart):
            print(f"{i + 1}. {item}")
            
        print(f"Total calories: {total_calories} calories")
        print(f"Food total: ${total_price:.2f}")

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
        
    def order(self):
        total_price = 0
        total_calories = 0
        cart = []
        
        while True:
            print()
            self.print_menu()
            print()
            user_selection = int(input("Select item # to add to cart, or enter 0 if you are ready to checkout: "))
            
            if user_selection == 0:
                break
            elif user_selection >= 1 and user_selection <= 6:
                menu_items = list(self.menu.keys())
                menu_selection = menu_items[user_selection - 1]
                
                item_price, item_calories = self.menu[menu_selection]
                
                total_price += item_price
                total_calories += item_calories
                cart.append(menu_selection)
            else:
                print("Invalid selection, press 0 if you are ready to checkout.")
                
        print()
        self.print_order_summary(cart, total_price, total_calories)
            
        return total_price
    
    def print_menu(self):
        print("Cheesecake Factory Menu:\n")
        
        i = 1
        
        for item, details in self.menu.items():
            price, calories = details
            print(f"{i}. {item} | Price: ${price:.2f}, Calories: {calories} cal")
            i += 1

    # User simply chooses from menu, calculates price and calories for each

class McDonalds(Restaurant):
    def __init__(self):
        # Compound menu - choose either sandwich or sandwich + meal
        meal_menu = {"Happy Meal": (3, 500), "Regular Meal": (5, 790), "Large Meal": (8, 1100)}
        sandwich_menu = {"Big Mac": (6, 450), "Quarter Pounder": (5, 500), "McChicken": (3, 350), "Cheese Burger": (3, 300)}
        
        menu = {"meals": meal_menu, "sandwiches": sandwich_menu}
        
        super().__init__(menu)
        
    def order(self):
        total_price = 0
        total_calories = 0
        cart = []
        
        while True:
            print()
            self.print_sandwich_menu()
            print()
            user_sandwich_selection = int(input("Select Sandwich # to add to cart, or enter 0 if you are ready to checkout: "))
            
            if user_sandwich_selection == 0:
                break
            elif user_sandwich_selection >= 1 and user_sandwich_selection <= 4:
                sandwich_items = list(self.menu["sandwiches"])
                sandwich_selection = sandwich_items[user_sandwich_selection - 1]
                sandwich_price, sandwich_calories = self.menu["sandwiches"][sandwich_selection]
                
                total_price += sandwich_price
                total_calories += sandwich_calories
                cart.append(sandwich_selection)
                
                print()
                self.print_meal_menu()
                print()
                user_meal_selection = int(input("Select your meal type, or type 0 for sandwich only: "))
                
                if user_meal_selection == 0:
                    continue
                if user_meal_selection >= 1 and user_meal_selection <= 3:
                    meal_items = list(self.menu["meals"])
                    meal_selection = meal_items[user_meal_selection - 1]
                    meal_price, meal_calories = self.menu["meals"][meal_selection]
                    
                    total_price += meal_price
                    total_calories += meal_calories
                    cart[-1] = cart[-1] + " " + meal_selection
                else:
                    print("Invalid meal selection, adding sandwich only to cart.")
            else:
                print("Invalid sandwich selection, try again.")
                
        print()
        self.print_order_summary(cart, total_price, total_calories)
        
        return total_price
        
    def print_sandwich_menu(self):
        print("Mcdonald's Sandwich Menu:\n")
        
        i = 1
        
        for item, details in self.menu["sandwiches"].items():
            price, calories = details
            print(f"{i}. {item} | Price: ${price:.2f}, Calories: {calories} cal")
            i+=1
    
    def print_meal_menu(self):
        print("Mcdonald's Meal Menu:\n")
        
        i = 1
        
        print(f"0. Sandwich only | Price: ${0:.2f}, Calories: 0 cal")
        for item, details in self.menu["meals"].items():
            price, calories = details
            print(f"{i}. {item} | Price: ${price:.2f}, Calories: {calories} cal")
            i+=1
    
       
class TatteBakery(Restaurant):
    def __init__(self):
        # Add $1 and 100 calories for each additional option on each item
        # When ordering, user must be prompted for each option - either "Y" or "N"
        menu = {"Almond Croissant": (3,400, ("butter", "egg")),
                    "Short Ribs Sandwich": (10,560, ("meat", "onions")),
                     "Chicken Pita": (8,450, ("toasted", "pickles")),
                     "Coffee": (2, 100, ("caramel", "whipped cream")),
                     }
        super().__init__(menu)
        
    def order(self):
        total_price = 0
        total_calories = 0
        cart = []
        
        while True:
            print()
            self.print_menu()
            print()
            user_selection = int(input("Select item # to add to cart, or enter 0 if you are ready to checkout: "))
            
            if user_selection == 0:
                break
            elif user_selection >= 1 and user_selection <= 4:
                menu_items = list(self.menu.keys())
                menu_selection = menu_items[user_selection - 1]
                
                item_price, item_calories, options = self.menu[menu_selection]
                
                total_price += item_price
                total_calories += item_calories
                cart.append(menu_selection)
                
                while True:
                    print()
                    self.print_options(menu_selection)
                    print()
                    option_selection = int(input("Select option # to add to your item, or enter 0 for no options: "))
                    
                    if option_selection == 0:
                        break
                    elif option_selection >= 1 and option_selection <= 2:
                        option = options[option_selection - 1]
                        total_price += 1
                        total_calories += 100
                        cart[-1] = cart[-1] + "+" + option
            else:
                print("Invalid selection, press 0 if you are ready to checkout.")
         
        print()
        self.print_order_summary(cart, total_price, total_calories)
        
        return total_price
        
    def print_menu(self):
        print("Tatte Bakery Menu:\n")
        
        i = 1
        
        for item, details in self.menu.items():
            price, calories, options = details
            print(f"{i}. {item} | Price: ${price:.2f}, Calories: {calories} cal | Additional Options: {options}")
            i += 1
              
    def print_options(self, item):
        print(f"Options for {item}:")
        
        i = 1
        print(f"0. No options | Price: ${0:.2f}, Calories: 0 cal")
        for option in self.menu[item][2]:
            print(f"{i}. {option} | Price: $1.00, Calories: 100 cal")
            i += 1
        
class DominosPizza(Restaurant): 
    def __init__(self):
        # User must choose a size and a choice
        size_menu = {"Small": (10, 500), "Medium": (13, 750), "Large": (16, 900)}
        choice_menu = {"Cheese": (2, 200), "Pepperoni": (5, 250), "Hawaiian": (3, 200), "Veggie": (4, 170), "BBQ Chicken": (6, 350)}
        
        menu = {"size": size_menu, "choice": choice_menu}
        
      
        super().__init__(menu)
        
        
    def order(self):
        total_price = 0
        total_calories = 0
        cart = []
        
        while True:
            print()
            self.print_size_menu()
            print()
            user_selection = int(input("Select your pizza size, or enter 0 if you are ready to checkout: "))
            
            if user_selection == 0:
                break
            elif user_selection <= 3 and user_selection >= 1:
                size_options = list(self.menu["size"].keys())
                size_selection = size_options[user_selection - 1]
                size_price, size_calories = self.menu["size"][size_selection]
                
                print()
                self.print_pizza_menu()
                print()
                user_selection = int(input("Select pizza choice: "))
                
                while user_selection > 5 or user_selection < 1:
                    print("Invalid selection, enter a number 1-5.\n")
                    self.print_pizza_menu()
                    print()
                    pizza_selection = int(input("Select pizza choice: "))
                    print()
                
                pizza_options = list(self.menu["choice"].keys())
                pizza_selection = pizza_options[user_selection - 1]
                pizza_price, pizza_calories = self.menu["choice"][pizza_selection]
                
                total_price += (size_price + pizza_price)
                total_calories += (size_calories + pizza_calories)
                pizza_order = f"{size_selection} {pizza_selection} Pizza"
                cart.append(pizza_order)
            else:
                print("Invalid selection, press 0 if you are ready to checkout.")
    
        print()
        self.print_order_summary(cart, total_price, total_calories)
        
        return total_price
    
    def print_size_menu(self):
       print("Dominos Sizes:\n")
       
       i = 1
       
       for size, details in self.menu["size"].items():
           price, calories = details
           print(f"{i}. {size} | Price: ${price:.2f}, Calories: {calories} cal")
           i+=1
   
    def print_pizza_menu(self):
       print("Dominos Pizza Menu:\n")
       
       i = 1
       
       for pizza, details in self.menu["choice"].items():
           price, calories = details
           print(f"{i}. {pizza} | Price: ${price:.2f}, Calories: {calories} cal")
           i+=1
            
    # User chooses size with each size having specific number of calories and price
    # User chooses type of pizza from list of above that adds a specific amount extra to the price based on choice along with specific calorie count 
    # Calculates total cost and total calories based on choice of size and pizza

class Chipotle(Restaurant): #To edit later customisable bowl
    def __init__(self):
        
        choice = {"Burrito": (8,120), "Bowl": (6,100)}
        beans = {}
        rice = {"White Rice": (), "Brown Rice": ()}
        protein = {"Carne Asada": (6,250),"Chicken Pastor": (4,300),"Barbacoa": (5,330)}
        toppings = {"Guac": (3,200),"Sour Cream": (2,100),"Corn": (2,70), "Pico Gallo": (3,60), "Hot Sauce": (1,20)}
        
        menu = {"Burrito or Bowl": choice, "White or Brown Rice": rice, "Protein": protein, "Toppings": toppings}
        super().__init__(menu)
    
    # User builds either bowl or burrito from scratch by choosing an option from each category while knowing both price and calorie count
    
    
def print_restaurant_names():
    print("Restaurants:\n")
    restaurants = ["Cheesecake Factory", "McDonald's", "Tatte Bakery", "Dominos Pizza", "Chipotle"]
    
    for i, r in enumerate(restaurants, start=1):
        print(f"{i}. {r}")
        
def print_areas():
    print("1. Fenway")
    print("2. Newbury")
    print("3. Downtown")
    print("4. Seaport")
    print("5. Backbay")
        
def calculate_delivery_cost(area, traffic_level):
    area_delivery_costs = {1: 2, 2: 2.5, 3: 2.5, 4: 2.5, 5: 2.5}
    if area in area_delivery_costs:
        delivery_cost = round(area_delivery_costs[area]*traffic_level, 2)
        
        return delivery_cost
    else:
        print("Invalid area number.")
        
                
def calculate_delivery_time(area, traffic_level):
    area_delivery_times = {1: 10, 2: 15, 3: 25, 4: 30, 5: 20}
    if area in area_delivery_times:
        delivery_time = int(area_delivery_times[area] * traffic_level)
        
        return delivery_time
    else:
        print("Invalid area number.")
    
          
def main():
    restaurants = [CheesecakeFactory(), McDonalds(), TatteBakery(), DominosPizza(), Chipotle()]
    
    print_restaurant_names()
    print()
    choice = int(input("Choose a restaurant by number: "))
    
    while choice > 5 or choice < 1:
        print_restaurant_names()
        print("Invalid selection, enter a number 1-5.\n")
        choice = int(input("Choose a restaurant by number: "))
        print()

    chosen_restaurant = restaurants[choice - 1]
    
    print_areas()
    print()
    print()
    area_number = int(input("Please enter your area number: ")) 
    print("____________________________________________________________________")
    
   
    while area_number > 5 or area_number < 1:
        print_areas()
        print()
        print()
        area_number = int(input("Please enter your area number: "))
        print("____________________________________________________________________")
     
   
    
    traffic_dict = {"no traffic": 1, "low traffic": 1.1, "high traffic": 1.3}
    traffic_type, traffic_level = rd.choice(list(traffic_dict.items()))
    
    delivery_cost = calculate_delivery_cost(area_number, traffic_level)
    delivery_time = calculate_delivery_time(area_number, traffic_level)
    food_cost = chosen_restaurant.order()
 
    print()
    print(f"Delivery cost: ${delivery_cost:.2f}")
    print(f"Grand total: ${delivery_cost + food_cost:.2f}")
    print(f"Estimated delivery time: {delivery_time} min due to {traffic_type}.")

main()

def test_main():
    r = DominosPizza()
    r.order()
    
#test_main()
