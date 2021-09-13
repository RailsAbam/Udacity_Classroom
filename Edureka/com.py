
#List
my_list = [10, 15, "minuted", 50, "seconds", 28, "Rails"] 


my_list[2] = 100 #Updating the  SECOND item in  this list
my_list .append(150)      #Adding an item to the END  list
my_list.insert(5, 250) #Adding an item in the index 5 part of the list
my_list.reverse()
print(my_list)


#Dictionary
courses = {1: "Python", 2:"Ruby", 3: "JavaScript", "four": "data science"}
courses[4] = "machine learning" #Updating the dictionary
print(courses)


#Tuples
tup = [10, 25 ,20 ,"tiger", "lion", "tiger", "bear", 25]
print(tup.count("tiger"))
print(tup)


#set
#unorder 
myset = {1,2,3,4,5,6,7,"team", "players", 2, 3}
print(myset)


#Type conversion
a = {100,200,300,400}
b = (500, 600, 700,800)
c = [a,b]
d =list(b) #Converting set to list
print(c)





