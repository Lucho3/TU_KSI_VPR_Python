amount=int(input("Enter number: "))
sum=0
for i in range(0,amount):
    number=int(input("Enter number: "))
    if number<0:
        sum+=number

print(sum)
