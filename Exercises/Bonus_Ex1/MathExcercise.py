import math

a=int(input("Please enter a:"))
b=int(input("Please enter b:"))
h=int(input("Please enter h:"))
r=int(input("Please enter r:"))

s=round((a+b)*h/2,2)
sCircle=round(math.pi*r*r,3)
pCircle=round(math.pi*2*r,3)

print("S of the trapeze is:" + str(s))
print("S of the circle is:"+str(sCircle))
print("P of the circle is:"+str(pCircle))