amount=int(input("Enter number: "))
multi=1
if amount<10:
    for i in range(0,amount):
         number=int(input("Enter number: "))
         while number>=1000:
            number=int(input("Enter new number: "))
         else:
            multi*=number

print(multi)
