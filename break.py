

manifest = [('bannas', 15), ('mattresses', 34), ('palm_oil', 42), ('machine', 120)]
weight = 0
item = []
for cargo in manifest:
    if weight >= 100:
        break
    else:
        item.append(cargo[0])
        weight = weight + cargo[1]
print(weight)
print(item)







#continue Key Word
fruits = ['orange', 'pinaple', 'strawberry', 'apple']
foods =  ['apple', 'apple','hummus', 'toast']

fruits_count = 0
for food in foods:
    if food not in fruits:
        print('Not fruits')
        continue
    fruits_count = fruits_count + 1
    print('Found a Fruits')
print('Total Fruit: ', fruits_count)