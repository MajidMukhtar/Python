# Let's build a robot barrista

print("Hello, welcome to our coffee shop")

#Getting the users name
name = input("What is your name?\n")

#Greeting the User with their own name
print("Hello " + name + ", thank you for coming in today.")

#Items that will be presented to User
menu = "Black coffee, French Vanilla, Cocunut Latte"

#Getting the users order
order = input("What can I get you? We offer " + menu + "\n")

#Acknolwedging and stating the users order to them
print("Oh, I also love " + order + "! Splendid choice!")

#Getting the number of items the user orders
numberOrder = int(input("How many " + order + " would you like? \n"))

#Calculating the total price
price = str(8 * numberOrder)

print("Your total today will be $" + price)