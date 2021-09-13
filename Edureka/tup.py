
from collections import namedtuple

lang = namedtuple("course", "name, technology")
stack = lang("data science","python" )

print(stack)