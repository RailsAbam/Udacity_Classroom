import array 
import array as arr


a = array.array('i',[2,  6, 6, 8 , 10])
b = a.pop()
print(a)


#Methods in array
c = arr.array('d',[10,15,20,25, 5.6])
c.append(55.4) #Add to the end of array but takes only one argument
c.extend([10.5,60.5]) #Added to the end of the array
c.insert(150, 100)
print(c)