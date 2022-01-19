n=int(input("Enter number: "))
sumEven=0
multiOdd=1
evenCount=0
for i in range(0,n):
        number=int(input("Enter number: "))
        if number%2==0:
            evenCount+=1
            sumEven+=number
        else:
            multiOdd*=number

if evenCount>0:
    print("Multiplication of odds: ",multiOdd)
    print("Avg of evens: ",sumEven/evenCount)
else:
    print("Multiplication of odds: ",multiOdd)
