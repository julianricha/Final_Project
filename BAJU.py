import random as rd

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        
    def print_order_summary(self, cart, total_price, total_calories):
        print("Order summary: ")
        for i, item in enumerate(cart):
            print(f"{i + 1}. {item}")
            
        print(f"Food total: ${total_price:.2f}")
        print(f"Total calories: {total_calories} calories")

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
            self.print_menu()
            
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
                
        self.print_order_summary(cart, total_price, total_calories)
            
        # May need to take this return value so we can add it to the delivery fee later.
        #return total_price
    
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
            self.print_sandwich_menu()
           
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
                
                self.print_meal_menu()
                user_meal_selection = int(input("Would you like to make it a meal?: "))
                
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
                
        self.print_order_summary(cart, total_price, total_calories)
        
        #return total_price
        
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
    
    
    def order_cart():
    # for next iteration
        pass
    def calculate_total_cost():
    # for next iteration
        pass
    
    
   
    
    
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

    
    
#main()

def test_main():
    mc = McDonalds()
    mc.order()

test_main()




