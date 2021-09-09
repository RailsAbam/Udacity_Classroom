

my_list = [1, 2, 3, 4, 5, "time"]
new_item = my_list.append("second") #Add new items to the list
print(my_list)

my_list1 = [10, 15 ,20 ,25]
new_1 = my_list1.clear() #Clearing the list
print(my_list1)


my_list2 = []
new_1 = my_list2.append(17) #Copying the list
new_1 = my_list2.copy()
print(my_list2)



print(my_list[::-1])


#List ilterating

for i in enumerate("Awesome"):
    print(i)


i = 0
while i < 5 :
    print(i)
    i += 1


for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        continue
    elif num > 5:
        break
    print(num)


capital_letters = []
for t in range(65,91):
    time = capital_letters.append(chr(t))
print(capital_letters[18:])



#Dictionaries


My_sons = {"Ruby":"F", "Rails": "M", "Clark": "M", "Clatibuk": "F"}
compare = My_sons["Ruby"] == ["Rails"]
print(compare)

# Another method of Creating a dictionary
step_sons = dict(key = "jason")
step_sons ["zenetha"] = "Girl"
step_sons["jannell"] = "girl"

print(step_sons.pop("key"))
print(step_sons.popitem())

grandsons = {}#updating a dict
grandsons.update(step_sons)
grandsons["tim"] = "Boy"
print(grandsons)


str1 = "ABC"
str2 = "123"

{str1[i]:str2[i] for i in range(0,len(str1))}
print(i)



d = {'a': 1, 'c': 3, 'e': 5} # [a, b .e] for keys
for k,v in d.items(): # [1, 5, 3] for values
    if (k,v ) in d.items():
     print(k,v)


#Tuples
x  = (1, 2, 2,  1,3, 3, )
#count1 = x.count(1)
count1 = x.count(3)
count1 = x.index(2) #Return the index the element falls
print(count1)


