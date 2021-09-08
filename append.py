

users = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
name = []

for item in users:
    if len(item):
        name.append(item.lower().replace(" ", " _ "))
print(name)