number=int(input("Enter number: "))
multi=1
sum=0

for numb in range (1,number+1):   
    sum+=numb
    multi*=numb

print(multi,sum)
