

#Guess = 20
Guess = 20
Guess = int(input("Guess a Number: "))

if Guess <= 10: 
    print("Guess is too low")
elif Guess >= 30: 
    print("Your is too High ")
elif Guess == 20: 
    print("Nice you corrected")


state = "Lagos"
#state = "Abuja", 8.5
#state = "Port Harcourt", 7.5
amount_of_purchase = 10

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


state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


