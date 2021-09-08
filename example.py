
#I can import this module in another file
#help() function to get imformation about this file.


b = 3
c = "word"
add = str(b) + " " + c #converting a number to  a string 
print(add) 


Name = (input(" What is your name: "))
Desc = (input("Describe  Your self: "))
Gerder = (input("What is Your Gerder ?(male/female: "))
Race = (input("What is your choice Car ? "))

statement = "Since you'r {} is and {} and also {} your choice car should be {}.".format(Name,Desc,Gerder,Race)
print(statement)




width =  140
Price_per_meter = 5 
window_height = (input("Enter Window Height: "))
window_width = (input("Enter window_width: "))

curtain_weight=  float( window_height)  * 0.75 + 20 
curtain_width= float(window_width ) + 15 

widths =  curtain_width / width 
total_cost = curtain_weight * widths
total_cost = (total_cost * 2) / 10

price = total_cost * Price_per_meter
result = "You will need {} meters of cloths for {}" .format(total_cost,price)
print(result)





