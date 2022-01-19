n=int(input("Enter number: "))
k=int(input("Enter number for comparison: "))
sum=0

for i in range(0,n):
    number=int(input("Enter number: "))
    if number>k:
        sum+=number
print(sum)
