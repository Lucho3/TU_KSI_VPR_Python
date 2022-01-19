n=int(input("Enter number: "))
k=int(input("Enter number for comparison: "))
sum=0
addedNumbers=0
for i in range(0,n):
        number=int(input("Enter number: "))
        if number>k:
            sum+=number
            addedNumbers+=1
if addedNumbers!=0:
        print(sum/addedNumbers)
    else:
        print(0)

