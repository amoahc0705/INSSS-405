#Hot>=50
#Warm 30-50
#Cold 0-30
#Extreme cold < 0

for x in range(7):
    temperature = int(input("enter temperature: "))
    if(int(temperature)) >= 50:
        print("Hot")
    elif(int(temperature) >=30 and int(temperature) <50):
        print("warm")
    elif(int(temperature) >=0 and int(temperature)<30):
        print("cold")
    elif(int(temperature) <0):
        print("Extreme cold")