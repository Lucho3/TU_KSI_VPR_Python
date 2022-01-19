amount=int(input("Enter number: "))
sum=0
if amount>=1 and amount<=1000:
    for i in range(0,amount):
         number=int(input("Enter number: "))
         sum+=number

print(sum/amount)
