

users = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
name = []

for item in users:
    if len(item):
        name.append(item.lower().replace(" ", " _ "))
print(name)


for x in enumerate("word"):
    print(x)
Name = "Ruby And rails"
print(Name.find("r"))


Name = "Ruby And rails"
print(Name[1].isalpha())

Name = "Ruby And rails"
print(Name.isspace())

name = "string"
print(name.rpartition("s"))



