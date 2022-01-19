amount=int(input("Enter number: "))
sumEven=0
sumOdd=0

for i in range(0,amount):
     number=int(input("Enter number: "))
     if number%2==0:
         sumEven+=number
     else:
         sumOdd+=number

print("Sum even: ",sumEven)
print("Sum odd: ",sumOdd)
