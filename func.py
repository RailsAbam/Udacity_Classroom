

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


