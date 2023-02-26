# Let's build a robot barrista
# Video Time: 11:00

print("Hello, welcome to our coffee shop")

# Getting and storing users name
name = input("What is your name?\n")

if name == "Ben":
  #print("You're not welcome here Ben. Get out!!!")
  reply = input("Are you evil? \n")
  if reply == "Yes":
    print("Get out of here you villain!")
    exit()
  else:
    print("Wow, a Ben that isn't evil. I like you!")
else:
  print("Hello " + name + ", thank you for coming in today.")

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