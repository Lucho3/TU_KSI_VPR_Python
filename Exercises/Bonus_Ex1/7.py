numb=int(input("Enter  number: "))
n=str(numb)
newNumber=''

for i in range(len(n)-1,-1,-1):
    newNumber+=n[i]

print(newNumber)
