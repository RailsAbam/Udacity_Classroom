
#For loop


cities = ["lagos", "abuja", "port harcort", "calaber"]
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)


states = ["benue", "ogun", "oyo", "enugu"]
capitalized_states = [] #Creeting a new list
for city in range (len(states)):
    capitalized_states.append(city) #adding the new list created
    states[index] = states[index].title()
print(states)


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for new_sentence in enumerate(sentence): #printing each element with the index
    print(new_sentence)  #By using enumerate function


#Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
for num1 in range(5,35,5):
        print(num1)


#Write a loop that will print out  every number divisable by 2
# 4 is the start of the num point of printing while 22 is the stop of range 2 is the divisable
for is_divisable in range(4, 22, 2):
    print(is_divisable)
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]


for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)




