


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#percentage 
#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
#print(total_bill)
tips = int(input("What percentage tip would you like to give 10, 12, or 15? "))
#print(tips)
person = int(input("How many people to split the bill? "))
#print(person)
percentage = ((total_bill * tips)/100)
total_bill = (total_bill + percentage)
each_person_pay = (total_bill / person)
print(each_person_pay)
round_bill = round(each_person_pay, 2)  #this will only give 1 decimal places 33.6

##to get two decimal places we can use format

round_bill = "{:.2f}".format(round_bill)
print(f"Each person should pay: ${round_bill}")