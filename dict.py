

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for (key,value) in cast.items():
    print("Actor : {}  Role:{}".format(key,value))



result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object,count in basket_items.items():
    if object in fruits:
        result += count
print("There are {} friuts in the basket".format(result))


for key,value in basket_items.items():
    if key in fruits:
        result += value
print(result)



fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object,count_value in basket_items.items():
    if object in fruits:
       
#if the key is in the list of fruits, add to fruit_count.
        fruit_count += count_value
#if the key is not in the list, then add to the not_fruit_count
 #   if object is not count_value:
        not_fruit_count += fruit_count
print("There are {} in fruit_count, and {} in not_fruit_count".format(fruit_count,not_fruit_count))







