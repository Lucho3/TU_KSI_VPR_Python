number=int(input("Enter your number:"))
print(" "*(number-1),"*")
for i in range(0,number-2):
         print("{0}{1}{2}{3}".format(" "*(number-i-1),"* "," "*i*2,"*"))
print(" *"*number)



