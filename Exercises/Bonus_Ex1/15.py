n=int(input("Enter number: "))
u=int(input("Enter number for comparison u: "))
v=int(input("Enter number for comparison v : "))
sum=0
addedNumbers=0

if u>v:
    for i in range(0,n):
        number=int(input("Enter number: "))
        if number>v and number<u:
            sum+=number
            addedNumbers+=1
    if addedNumbers!=0:
        print(sum/addedNumbers)
    else:
        print(0)
else:
    print("u must be grater than v")
