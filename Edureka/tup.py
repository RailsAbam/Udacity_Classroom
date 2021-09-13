
from collections import namedtuple
from collections import  deque
from collections import ChainMap
from collections import Counter

lang = namedtuple("course", "name, technology")
stack1 = lang("data science","python" )
print(stack1)

lang1 = namedtuple("course", "name, technology")
stack = lang1._make(["Django", "Python"])
print(stack)

#Deque
name = ['R', 'a', 'i', 'l']
tech = deque(name)
tech.append("and") #Adding value at the end of the deque
tech.appendleft("name") #This function adds value to the FRONT of the deque
tech.pop() #Remove the last element on the list
tech.popleft() #This remove the FIRST element on the deque list
print(tech)