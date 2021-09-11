

#Functions
#name = "Ruby"
#language = "Ruby and Rails"
def text(name , language ):
    return "I love {}, So i like her to learning {}.".format(name,language)
print(text("Ruby", "Rails"))
lovely = "Dear"
#Functions with key arguments
def text(name = "Ruby", language = "Rails and Ruby" ):
    return "I love {}, So i like her to learning {}, So learn harder {}.".format(name,language,lovely)
print(text())


def add(a = 5, b = 20):
    return a + b
print(add(10, 25)) # This overwrite  the first argument  


def times( * args, b = 10): #This offers opportunity for more arguments
  return args

print(times([2 + 3 + 5 + 5]))


def trail ( t1 ,t2 , t3 ,t4):
    return  t1 + t2 + t3 + t4
print(trail(*[10, 20, 30 , 40 ]))

def line(t,i,m,e):
    return t + i + m * e
nums = [ 5, 5 , 5, 2]
num1 = {2,2,2,4}
num2 = (4, 4,4 ,5)
print(line(*nums)) #unpacking a value
print(line(2, 2 , 2 ,4)) # * args  does work in a set
print(line(*num2))


#Function with unknown number of arguments
def select(** kwargs):
    return (kwargs)
print(select(b = 10, name = "ruby", t5 = 5 + 3))

#Unpackingthe value 
def sum_all( a, b , c):
    return (a + b * c)

data = dict(a = 2 , b = 4, c = 5)
print(sum_all(** data))


def test():
    x  = 3
    return x
    name = "rails"

name = "tim"
print(test())
#print(globals())

tag = 0 #Needs to dig more on this
def till():
    global tag
    tag += 2
print(till())


#nested Functions and calls

def caller_1 (a):
    def caller_2(b):
        def caller_3(c):
            return  a + b 
        return caller_3
    print(caller_2(3))
print(caller_1(5))


book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
     if word not in word_counter:
       word_counter[word] = 1
     else:
       word_counter[word] =+ 1
print(word_counter)

