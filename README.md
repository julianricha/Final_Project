# Push/Pull Process
Main python file for both of us (BAJU.py)

Always pull before working

Always push after saving and finishing

For Pushing:
1. Save file
2. Add file (git add filename.py)
3. Commit (git commit -m "message")
4. Push (git push origin main)

For Pulling
1. Open gitbash in Final Project folder
2. Git pull origin main
3. Most recent file commit will appear in folder
4. Work on that python file and push after done





# Final Project
# Food Ordering App of Julian and Bader: BAJU

## Project Topic: Food Ordering App 
This project aims to develop a comprehensive Python application that leverages a food ordering system that allows users to order food from the menu of the restaurant of their choice, be able to track their order such as estimated delivery time with traffic taken into account based on location, breakdown of order cost, and be able to apply to an optional membership offered by the app for discounts. The application will utilize object oriented programming and inheritance for both restaurants and user functionality, and will be using a graphical user interface to provide a friendly and dynamic interaction with the user. The primary objective is to build a user-friendly and efficient app for users of different locations and appetites to order food online through delivery, while having the option of using a monthly membership to have users be excluded from delivery fees, services fees, tax fees, and be able to apply discounts. 

## Git Repository: 
https://github.com/julianricha/Final_Project 

## Project Objectives: 
- To develop a Python application that allows users to order food through delivery, have a breakdown of the order cost, estimated delivery time, and calculate total calories of order
- Implement object oriented programming and inheritance for restaurants and user functionalities

## Deliverables: 
- A fully functional Python application of a food ordering system 
- A report detailing the program's efficiency and behavior with orders from different restaurants. 
- A project presentation that summarizes the project's objectives, development process,  challenges encountered, and learning outcomes.
- Calculates price and calorie count of all items along with options.

## How to use Project:
Run program and follow the steps in the command line based on your desire of choice. Below are the details of each restaurant for you to utilize the full BAJU experience.

### Cheesecake Factory: User simply chooses items from the given menu, calculates calories and price.
### Mcdonalds: User chooses a sandwich from the sandwich menu with each having a set price and calorie count. Users are then prompted to choose whether they want the sandwich only, or want it as a Happy, Medium, or Large meal. Each meal also has a set price and calorie count since it comes with fries and a drink, so if the user chooses a meal, additional price and calorie calculations will occur.
### Tatte Bakery: User chooses from given menu, but is also given the option to add extra topping to selected item. Menu is a dictionary with item as key, and price, calorie count, and toppings tuple as value. Every option increases the price by 2 dollars and calorie count by 100 dollars.
### Dominos: User chooses pizza size which has set price and calorie count, and is then required to choose pizza choice which also has set price and calorie count. Calculates total calories and price based on the number of pizzas ordered as well as sizes and pizza choice.
### Chipotle: Users build order from scratch here. Users are first prompted to choose between bowl or burrito, then choose between white or brown rice, then black or pinto beans, then choose protein, then have the option of adding additional toppings as much as they want. Every single selection accounts for the calculated price and calories. User is required to choose before making additional toppings.

## Document Basic Functionalities 
- User Interaction: Ability to allow users to choose from a variety of restaurants and add items to the cart based on the restaurants menu
- Customizable Order: Allow users to customize orders based on chosen restaurant and be able to calculate the cost of the customizable order. A customizable order can be creating an order from scratch, or choosing stuff like toppings to a specific order, rather than just having to choose from a menu and adding to cart
- Total Cost: Display a total breakdown of order cost based on user menu choices, sizes, and other fees.
- Calorie Calculator: Calculates total calories of customizable order after checking out for users to stay on track of dietary restrctions.
- Delivery time: Based on both restaurant’s location and user location, we can display not only the delivery time, but also account for possible traffic that might delay an order

