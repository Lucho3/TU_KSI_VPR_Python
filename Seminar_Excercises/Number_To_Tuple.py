numb=input("Enter your number:")
tup=tuple()
for i in range(len(numb)):
    tup+=tuple(numb[i])

print(tup)


numb1=input("Enter your number:")
tup1=tuple()
for i in range(len(numb1)-1,-1,-1):
    tup1+=tuple(numb1[i])

print(tup1)
