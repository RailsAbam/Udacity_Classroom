

altitude = 10000
speed = 250
propulsion = "propeller"


if altitude < 10000 and speed > 100:
    print("Land") #False

if (propulsion == "Jet" or propulsion == "TurboProp") and speed < 300 and altitude > 20000:
    print("Take off") #False


if not (speed > 400 and propulsion == "propeller" ):
    print("Fail Landing") #True

if (altitude > 500 and speed > 100) or not propulsion == "propeller":
    print(False)    #True


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for i in tokens:
    if tokens[0] == "<" and tokens[-1] == ">":
        count += 1
print(count)


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
for sub in items:
    html_str += "<li>{}</li>\n".format(sub)
    html_str += "</ul>" 
print(html_str) 


