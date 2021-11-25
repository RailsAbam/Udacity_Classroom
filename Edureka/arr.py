import array
import array as arr

a = array.array('i',[2,  6, 6, 8 , 10])
b = a.pop()
print(a)


#Methods in array
c = arr.array('d',[10,15,20,25, 5.6])
print(c)
c.append(55.4) #Add to the end of array but takes only one argument
c.extend([10.5,60.5]) #Added to the end of the array
print(c)
c.insert(1,400)
print(c)

E = arr.array('q', [2,4,5,9, 6,8])
print(len(E))
print(E)

#Concatenation
a = arr.array('i', [5,6,7,8,9])
print(a[0:3])
c = arr.array('i',[10,11,12,13])
d = arr.array('i')
d = (a + c)
print(d)
#For Loop in array
for num in d[0:4]:
    print(num)



