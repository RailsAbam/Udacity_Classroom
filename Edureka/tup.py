
from collections import namedtuple

lang = namedtuple("course", "name, technology")
stack1 = lang("data science","python" )
print(stack1)

lang1 = namedtuple("course", "name, technology")
stack = lang1._make(["Django", "Python"])
print(stack)