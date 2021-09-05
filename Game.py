

#Guess = 20
Guess = 20
Guess = int(input("Guess a Number: "))

if Guess <= 10: 
    print("Guess is too low")
elif Guess >= 30: 
    print("Your is too High ")
elif Guess == 20: 
    print("Nice you corrected")



State = "Lagos", 10.5
state = "Abuja", 8.5
state = "Port Harcourt", 7.5
amount_of_purchase = "$10"
if state == "Lagos":
    total_tax = 0.75
    total_cost = amount_of_purchase *(1 + total_tax)
    cost = "Since you're from  {}, your total cost is {}.". format(state,total_cost)

elif state == "Abuja":
    total_tax = 0.95
    total_cost = amount_of_purchase * (1 + total_tax)
    cost = "Since you're from {}, your total cost is {}.".format(state,total_cost)

elif state == "Port Harcourt":
    total_tax = 0.89
    total_cost = amount_of_purchase * (1 + total_tax)
    cost = "Since you're  from {}, your total cost is {}.".format(state,total_tax)

print(cost)