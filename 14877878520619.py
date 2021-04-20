# My name is Amir Ali Karimi 
# This app is about second degree equation
import math
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
delta = (b**2-4*a*c)
if delta == 0 :
                x=(-b)/(2*a)
                print("moadele yek rishe haghighi darad")
                print(x)
if delta<0 :
                print ("in moadele be ezaye hich meghdar rishe haghghi nadarad")            
else:
                x1 = (-b-(math.sqrt(delta)))/(2*a)
                x2 = (-b+(math.sqrt(delta)))/(2*a)
                print("moadele do rishe haghighi darad")
                print(x1)
                print(x2)