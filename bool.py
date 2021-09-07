

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
