
name = 'Rails'
def helllo(name):
    print("Hello", name)

print(helllo(name))


def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return( "{} week(s) and {} day(s)".format(weeks, remainder))
print(readable_timedelta(4))


#Lamda Expression
def double(x):
    return x * 2
print(double(3))

double = lambda x: x * 4
print(double(2))

add = lambda x,y: x * y
print(add(5,10))

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

#Lambda Expression
mean = lambda num_list: sum(num_list) / len(num_list)
averages = list(map(mean,numbers))
print(averages)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)


is_short = lambda name: len(name) < 10
short_cities = list(filter(is_short,cities))
print(short_cities)



how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)