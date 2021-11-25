

check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2, num):
        if (num % 1) == 1:
            print('{} is NOT a prime number, because {} is a factor of {}'.format(num, i, num))
            continue
        if i == num -1:    
            print("{} IS a prime number".format(num))


#Zip Function
manifest = [('bannas', 15), ('mattresses', 34), ('palm_oil', 42), ('machine', 120)]

weight, items = zip(*manifest)
print(weight)
print(items)


item = ['bannas','mattresses', 'palm_oil',  'machine', ]
weights = [15, 30, 50, 43, 20]

for item, weights in zip(item, weights):
    print(item, weights)

items = ['mango', 'Beans', 'Rice', 'Garri']
for item,num in zip(range(len(items)),items):
    print(item, num)

for i, num in enumerate(items):
    print(i, num)




cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for  height,cast in enumerate(cast):
    if heights in heights and cast not in cast:
        cast = (cast,height)
print(cast)








x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for x,y,x in zip(x_coord, y_coord,z_coord,labels):
    print()