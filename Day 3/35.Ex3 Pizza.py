# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small = 15
medium = 20 
large = 25
bill = 0
if size == "S":
  bill = small
  if add_pepperoni == "Y":
    bill = small + 2
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}")
  else:
    print(f"You final bill is: ${bill}")  

if size == "M":
  bill = medium
  if add_pepperoni == "Y":
    bill = medium + 2
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}")
  else:
    print(f"You final bill is: ${bill}")

if size == "L":
  bill = large
  if add_pepperoni == "Y":
    bill = large + 2
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}")
  else:
    print(f"You final bill is: ${bill}")
    
    